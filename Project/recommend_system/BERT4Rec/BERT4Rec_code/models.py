from typing import Optional

import pytorch_lightning as pl
import torch
import torch.nn as nn
from torch.nn import Linear
from torch.nn import functional as F


# y_pred: 예측 추천
# y_true: 실제 소비한 아이템
# mask: 마스크
def masked_accuracy(y_pred: torch.Tensor, y_true: torch.Tensor, mask: torch.Tensor):

    # tensor([[-1.1839, -0.2547, -1.2708],
    #         [ 0.6713,  0.0494, -0.2655],
    #         [-0.3116,  0.7832, -1.2234],
    #         [-0.6373,  0.1265, -1.8030],
    #         [-0.1249, -1.7748,  1.2657]])

    # 각 텐서의 최대 값을 추출, 인덱스를 반환
    # dim = 0이면 열을 기준으로, dim = 1이면 행을 기준으로 반환
    # 각 유저별로 추천해줄 수 있는 아이템 중 확률이 가장 높은 것을 반환
    _, predicted = torch.max(y_pred, 1)


    y_true = torch.masked_select(y_true, mask)
    predicted = torch.masked_select(predicted, mask)

    acc = (y_true == predicted).double().mean()

    return acc


def masked_ce(y_pred, y_true, mask):

    loss = F.cross_entropy(y_pred, y_true, reduction="none")

    loss = loss * mask

    return loss.sum() / (mask.sum() + 1e-8)


class Recommender(pl.LightningModule):
    def __init__(
        self,
        vocab_size,
        channels=128,
        cap=0,
        mask=1,
        dropout=0.4,
        lr=1e-4,
    ):
        super().__init__()

        self.cap = cap
        self.mask = mask

        # 학습률, dropout율, 영화 종류
        self.lr = lr
        self.dropout = dropout
        self.vocab_size = vocab_size

        # 아이템 임베딩
        # 전체 아이템에 대한 임베딩
        # 나중에 배치에 있는 아이템만 추출
        # 16만 x 128 크기
        self.item_embeddings = torch.nn.Embedding(
            self.vocab_size, embedding_dim=channels
        )

        # 포지션 임베딩
        self.input_pos_embedding = torch.nn.Embedding(512, embedding_dim=channels)

        # Trm 인코더 구현
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=channels, nhead=4, dropout=self.dropout
        )

        # bert 인코더는 Trm 인코더 6개의 층을 쌓아서 구현
        self.encoder = torch.nn.TransformerEncoder(encoder_layer, num_layers=6)

        # 최종 출력하기 위한 FFN
        # 최종 59047개의 출력
        self.linear_out = Linear(channels, self.vocab_size)

        # dropout
        self.do = nn.Dropout(p=self.dropout)

    def encode_src(self, src_items):
        # 아이템 임베딩
        # 배치 크기: 32 > 32명의 유저
        # 각 유저 히스토리는 120개의 아이템이 존재
        # 각 아이템은 128차원으로 임베딩
        # 따라서 32 x 120 x 128 차원으로 임베딩
        src_items = self.item_embeddings(src_items)

        # src_items는 하나의 배치에 아이템 임베딩
        # batch x 각 유저의 히스토리 내 아이템 개수 => 32 x 120
        batch_size, in_sequence_len = src_items.size(0), src_items.size(1)

        # torch.arange(0, 120): numpy와 동일 tensor([0 ~ 119])
        # torch.unsqueeze(0): dimension idx 0에 1삽입 > shape = 32 >> shape = (1, 32)
        # torch.unsqueeze(1): dimension idx 1에 0삽입 > shape = 32 >> shape = (32, 1)
        # 32, 120 크기 positional tensor 생성
        pos_encoder = (
            torch.arange(0, in_sequence_len, device=src_items.device)
            .unsqueeze(0)
            .repeat(batch_size, 1)
        )

        # 32 x 120 행렬을 생각해볼 때
        # 각 행에 대해 열은 아이템을 의미하며, 순서도 있음 [0, 1, 2, 3, ... ,119]
        # pos_encoder가 바로 그 위치를 나타내기 때문에 곧바로 임베딩 적용가능

        # input_pos_embedding 크기: 512 x dim = 512 x 128
        # 512개의 자리에 대한 각 임베딩
        # input_pos_embedding(pos_encoder): 32 x 120 x 128 크기
        pos_encoder = self.input_pos_embedding(pos_encoder)

        # pos_embedding + item_embedding
        src_items += pos_encoder

        # src_item 차원 재배치
        # 120 x 32 x 128으로 재배치
        # view의 경우 값을 차례대로 일렬로 배치했을 때 배치된 대로 값이 재배치 되지만
        # permute의 경우 값이 32 x 120 행렬에서 120 x 32 행렬로 각 원소에 해당하는 128차원 임베딩이 유지된 채로 값이 행과 열이 재배치
        src = src_items.permute(1, 0, 2)

        # position x user x item embedding으로 입력
        src = self.encoder(src)

        # 다시 각 유저에 대해 position x item embedding으로 값을 반환
        return src.permute(1, 0, 2)

    def forward(self, src_items):
        # 예측을 만들어내는 메소드
        src = self.encode_src(src_items)

        # torch.nn.Linear(in_feat, out_feat)
        # y = xA^T + b를 적용한 결과
        # 이 때 32명의 120개의 아이템 임베딩(128차원)을 입력으로 59047개의 출력을 뽑아내야 함
        # 따라서 Linear(128, vocab_size)
        out = self.linear_out(src)

        return out

    def training_step(self, batch, batch_idx):
        # 바로 실행
        # batch에는 위에서의 out과 label이 담겨있음
        src_items, y_true = batch

        # forward 실행
        y_pred = self(src_items)

        y_pred = y_pred.view(-1, y_pred.size(2))
        y_true = y_true.view(-1)

        src_items = src_items.view(-1)
        mask = src_items == self.mask

        loss = masked_ce(y_pred=y_pred, y_true=y_true, mask=mask)
        accuracy = masked_accuracy(y_pred=y_pred, y_true=y_true, mask=mask)

        self.log("train_loss", loss)
        self.log("train_accuracy", accuracy)

        return loss

    def validation_step(self, batch, batch_idx):
        # epoch가 끝날 때 실행
        src_items, y_true = batch

        y_pred = self(src_items)

        y_pred = y_pred.view(-1, y_pred.size(2))
        y_true = y_true.view(-1)

        src_items = src_items.view(-1)
        mask = src_items == self.mask

        loss = masked_ce(y_pred=y_pred, y_true=y_true, mask=mask)
        accuracy = masked_accuracy(y_pred=y_pred, y_true=y_true, mask=mask)

        self.log("valid_loss", loss)
        self.log("valid_accuracy", accuracy)

        return loss

    def test_step(self, batch, batch_idx):
        # 학습 종료 직전 테스트 실행
        src_items, y_true = batch

        y_pred = self(src_items)

        y_pred = y_pred.view(-1, y_pred.size(2))
        y_true = y_true.view(-1)

        src_items = src_items.view(-1)
        mask = src_items == self.mask

        loss = masked_ce(y_pred=y_pred, y_true=y_true, mask=mask)
        accuracy = masked_accuracy(y_pred=y_pred, y_true=y_true, mask=mask)

        self.log("test_loss", loss)
        self.log("test_accuracy", accuracy)

        return loss

    def configure_optimizers(self):
        optimizer = torch.optim.Adam(self.parameters(), lr=self.lr)
        scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(
            optimizer, patience=10, factor=0.1
        )
        return {
            "optimizer": optimizer,
            "lr_scheduler": scheduler,
            "monitor": "valid_loss",
        }
