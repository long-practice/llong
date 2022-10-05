import random

import pandas as pd
import pytorch_lightning as pl
import torch
from pytorch_lightning.callbacks import ModelCheckpoint
from pytorch_lightning.loggers import TensorBoardLogger
from torch.utils.data import DataLoader

from models import Recommender
from data_processing import get_context, pad_list, map_column, MASK


# 80%는 그대로 반영
# 20%는 마스킹
def mask_list(l1, p=0.8):

    l1 = [a if random.random() < p else MASK for a in l1]

    return l1


# 마지막 5개에 대해 절반만 마스킹
def mask_last_elements_list(l1, val_context_size: int = 5):

    l1 = l1[:-val_context_size] + mask_list(l1[-val_context_size:], p=0.5)

    return l1


class Dataset(torch.utils.data.Dataset):
    # Dataset에는 userId, 그룹화 시킨 df, split, 이전 기록 크기를 전달
    def __init__(self, groups, grp_by, split, history_size=120):
        self.groups = groups
        self.grp_by = grp_by
        self.split = split
        self.history_size = history_size

    def __len__(self):
        return len(self.groups)

    def __getitem__(self, idx):
        # group: User
        group = self.groups[idx]

        # 해당 유저에 대한 df
        df = self.grp_by.get_group(group)

        # 어떤 유저의 context 생성(시청 영화 목록 생성)
        context = get_context(df, split=self.split, context_size=self.history_size)

        # 선정된 시청 영화 목록에 매핑되는 idx를 리스트로 변경
        trg_items = context["movieId_mapped"].tolist()

        # 선정된 시청 영화 목록을 마스킹(방법은 위에)
        if self.split == "train":
            src_items = mask_list(trg_items)
        else:
            src_items = mask_last_elements_list(trg_items)

        # 길이가 120 이하인 아이템들은 padding
        # 절반은 left, 절반은 right padding
        # left 방식과 right 방식 차이는 data_processing.py 참고
        pad_mode = "left" if random.random() < 0.5 else "right"
        trg_items = pad_list(trg_items, history_size=self.history_size, mode=pad_mode)
        src_items = pad_list(src_items, history_size=self.history_size, mode=pad_mode)

        # torch.tensor로 변환, 반환
        src_items = torch.tensor(src_items, dtype=torch.long)
        trg_items = torch.tensor(trg_items, dtype=torch.long)

        return src_items, trg_items


def train(
    data_csv_path: str,
    log_dir: str = "recommender_logs",
    model_dir: str = "recommender_models",
    batch_size: int = 32,
    epochs: int = 2000,
    history_size: int = 120,
):
    data = pd.read_csv(data_csv_path)

    data.sort_values(by="timestamp", inplace=True)

    # mapping > movieId: number(2부터) (총: 59047개의 key)
    # inverse_mapping > number: movieId
    data, mapping, inverse_mapping = map_column(data, col_name="movieId")

    # grp_by_train은 data df를 userId로 그룹화
    # user_Id: 해당 row의 인덱스 list
    grp_by_train = data.groupby(by="userId")

    # grp_by_train.groups의 type은 pandas.io.formats.printing.PrettyDict
    # 각 userId를 순차적으로 groups에 저장(실제로는 key값이 저장)
    groups = list(grp_by_train.groups)

    # train_data, val_data 분할
    # Dataset에는 userId, 그룹화 시킨 df, split, 이전 기록 크기를 전달
    # 최종적으로 120개의 아이템들 중 20%가 마스킹, 패딩된 상태로 생성
    # 반환은 torch.tensor
    # torch.utils.data.Dataset은 sample(feature)과 label을 저장
    train_data = Dataset(
        groups=groups,
        grp_by=grp_by_train,
        split="train",
        history_size=history_size,
    )
    val_data = Dataset(
        groups=groups,
        grp_by=grp_by_train,
        split="val",
        history_size=history_size,
    )

    print("len(train_data)", len(train_data))
    print("len(val_data)", len(val_data))

    # torch.utils.data.DataLoader는 저장한 Dataset을 iterable로 감싸주는 역할
    train_loader = DataLoader(
        train_data,
        batch_size=batch_size,
        num_workers=10,
        shuffle=True,
    )
    val_loader = DataLoader(
        val_data,
        batch_size=batch_size,
        num_workers=10,
        shuffle=False,
    )

    # 모델 생성
    # 대략 16만 개의 movieId를 vocab_size로 생성
    # +2: 의 이유는 pad와 mask
    # 학습률: 0.0001, dropout: 0.3
    model = Recommender(
        vocab_size=len(mapping) + 2,
        lr=1e-4,
        dropout=0.3,
    )

    # logger 객체 생성
    logger = TensorBoardLogger(
        save_dir=log_dir,
    )

    # checkpoint 객체 생성
    checkpoint_callback = ModelCheckpoint(
        monitor="valid_loss",
        mode="min",
        dirpath=model_dir,
        filename="recommender",
    )

    # PyTorch Lightning
    # PyTorch에 대한 고 수준 인터페이스 제공, 오픈소스 라이브러리
    # GPU, TPU 설정, 16-bit precision, 분산학습 등 복잡한 조건에서 실험을 할 경우 코드도 복잡
    # 하나의 코드 스타일로 자리 잡기 위해 탄생

    # PyTorch에서 Dataset, Dataloader, train/valid/test loop 등을 적용
    # PyTorch Lightning에서는 아래와 같이 두 줄로 해결가능

    # Trainer는 모델 학습에 관여되는 engineering을 담당하는 클래스
    # epoch, batch 상태, 로그 생성까지 담당

    # Lightning Module은 모델 내부 구조를 설계하는 resarch & science 클래스
    # 모델의 구조나 데이터 전처리, 손실함수 등 설정 등을 통해 모델을 초기화
    trainer = pl.Trainer(
        max_epochs=epochs,
        gpus=1,
        logger=logger,
        callbacks=[checkpoint_callback],
    )
    trainer.fit(model, train_loader, val_loader)
    result_val = trainer.test(dataloaders=val_loader)

    output_json = {
        "val_loss": result_val[0]["test_loss"],
        "best_model_path": checkpoint_callback.best_model_path,
    }

    print(output_json)

    return output_json


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("--data_csv_path")
    parser.add_argument("--epochs", type=int, default=500)
    args = parser.parse_args()

    train(
        data_csv_path=args.data_csv_path,
        epochs=args.epochs,
    )
