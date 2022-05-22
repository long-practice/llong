# 2019 카카오 개발자 겨울 인턴십
# 호텔 방 배정
# https://programmers.co.kr/learn/courses/30/lessons/64063

import sys
sys.setrecursionlimit(int(1e5))


def solution(k, room_number):
    answer = []
    parent = {}

    def find(x):
        if x in parent.keys():
            parent[x] = find(parent[x])
        else:
            parent[x] = x + 1
        return parent[x]

    for room in room_number:
        x = find(room)
        answer.append(x - 1)

    return answer