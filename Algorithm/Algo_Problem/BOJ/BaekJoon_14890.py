# 경사로

# 단순 구현문제처럼 보이지만 생각보다 어떻게 구현해야 효율적으로 구현할 수 있을지 애매했음
# 이번 문제처럼 여러가지 구현문제를 풀어가면서 나름대로 문제해결방식을 갖춰나가는 것도 필요

import sys
input = sys.stdin.readline

N, L = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]

def check_road(road):
    is_slope = [False for _ in range(N)]
    # 왼쪽에서부터 경사로 배치
    i = 1
    while i < N:
        if road[i] - road[i - 1] > 1:
            return False
        if road[i] - road[i - 1] == 1:
            if i - L < 0:
                return False
            else:
                p = road[i - 1]
                for j in range(i - L, i):
                    is_slope[j] = True
                    if road[j] != p:
                        return False
        i += 1

    # 오른쪽에서부터 경사로 배치
    # 만약 경사로를 배치해야할 곳에 경사로가 있다면 지나갈 수 없는 길
    i = N - 2
    while i >= 0:
        if road[i] - road[i + 1] > 1:
            return False
        if road[i] - road[i + 1] == 1:
            if i + L >= N:
                return False
            else:
                p = road[i + 1]
                for j in range(i + 1, i + L + 1):
                    if road[j] != p or is_slope[j]:
                        return False
        i -= 1

    return True

answer = 0
for k in range(N):
    if check_road(board[k]):
        answer += 1
    if check_road(list(zip(*board))[k]):
        answer += 1
print(answer)
