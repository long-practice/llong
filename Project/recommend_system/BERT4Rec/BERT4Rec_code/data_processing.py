import random

import numpy as np
import pandas as pd

PAD = 0
MASK = 1


def map_column(df: pd.DataFrame, col_name: str):
    """
    Maps column values to integers
    :param df:
    :param col_name:
    :return:
    """
    # ratings.csv를 timestamp에 정렬
    # mapping > movieId: number(2부터)
    # inverse_mapping > number: movieId
    values = sorted(list(df[col_name].unique()))
    mapping = {k: i + 2 for i, k in enumerate(values)}
    inverse_mapping = {v: k for k, v in mapping.items()}

    # 최종적으로 df에 [movieID_mapped] = idx
    # 나중에 idx로부터 movieId 호출 가능(inverse_mapping)
    df[col_name + "_mapped"] = df[col_name].map(mapping)

    return df, mapping, inverse_mapping


def get_context(df: pd.DataFrame, split: str, context_size: int = 120, val_context_size: int = 5):
    """
    Create a training / validation samples
    Validation samples are the last horizon_size rows
    :param df:
    :param split:
    :param context_size:
    :param val_context_size:
    :return:
    """
    # end_index: 10 ~ df.shape[0] ~ val_context_size 중 랜덤
    if split == "train":
        end_index = random.randint(10, df.shape[0] - val_context_size)
    elif split in ["val", "test"]:
        end_index = df.shape[0]
    else:
        raise ValueError

    # 예를 들어 df의 행 개수가 440개(어떤 유저가 시청한 영화가 440개)
    # 그렇다면 무작위로 설정한 end_index는 422일 때
    # df[302:422]가 context로 반영
    # 즉, 어떤 유저의 302부터 421까지 120개의 아이템이 context

    # 훈련 데이터의 경우 랜덤으로 생성하지만
    # 검증, 테스트 데이터의 경우 가장 나중 120개만 선정

    # 임의로 선정한 end_index 앞에 120개부터 context 구성
    start_index = max(0, end_index - context_size)

    # 그룹화된 df에서 start_index부터 end_index까지 구성
    context = df[start_index:end_index]

    return context


def pad_arr(arr: np.ndarray, expected_size: int = 30):
    """
    Pad top of array when there is not enough history
    :param arr:
    :param expected_size:
    :return:
    """
    arr = np.pad(arr, [(expected_size - arr.shape[0], 0), (0, 0)], mode="edge")
    return arr


def pad_list(list_integers, history_size: int, pad_val: int = PAD, mode="left"):
    """

    :param list_integers:
    :param history_size:
    :param pad_val:
    :param mode:
    :return:
    """
    # pad_mode: left > [pad, pad, list]
    # pad_mode: right > [list, pad, pad]
    if len(list_integers) < history_size:
        if mode == "left":
            list_integers = [pad_val] * (history_size - len(list_integers)) + list_integers
        else:
            list_integers = list_integers + [pad_val] * (history_size - len(list_integers))

    return list_integers


def df_to_np(df, expected_size=30):
    arr = np.array(df)
    arr = pad_arr(arr, expected_size=expected_size)
    return arr


def genome_mapping(genome):
    genome.sort_values(by=["movieId", "tagId"], inplace=True)
    movie_genome = genome.groupby("movieId")["relevance"].agg(list).reset_index()

    movie_genome = {a: b for a, b in zip(movie_genome['movieId'], movie_genome['relevance'])}

    return movie_genome

