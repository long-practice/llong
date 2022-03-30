# 경찰차


# 최초 경찰차의 위치(1,1), (N, N)
# 단순 완전탐색으로 접근하게 될 시 2 ** 1000의 연산이 소요
# 다이나믹 프로그래밍을 이용하여 중복되는 계산을 하지 않도록함
# 예를 들어 DP[A][B]는 A번 사건을 1번 경찰차가, B번 사건을 2번 경찰차가 해결했을 때
# 다음 번 이동 위치까지의 최소 거리가 저장되게 됨

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e5))

N = int(input().rstrip())
W = int(input().rstrip())
pos = [(1, 1), (N, N)]
for _ in range(W):
    pos.append(tuple(map(int, input().rstrip().split(' '))))

DP = [[-1 for _ in range(W + 2)] for _ in range(W + 2)]


def dist(X, Y):
    return abs(pos[X][0] - pos[Y][0]) + abs(pos[X][1] - pos[Y][1])


def get_shortest_dist(A, B):
    if A > W or B > W:
        return 0
    if DP[A][B] != -1:
        return DP[A][B]
    else:
        next_pos = max(A, B) + 1
        move_A = get_shortest_dist(next_pos, B) + dist(next_pos, A)
        move_B = get_shortest_dist(A, next_pos) + dist(next_pos, B)

        DP[A][B] = min(move_A, move_B)
        return DP[A][B]


def trace(A, B):
    if A > W or B > W:
        return

    next_pos = max(A, B) + 1
    trace_A = dist(next_pos, A)
    trace_B = dist(next_pos, B)

    if DP[next_pos][B] + trace_A < DP[A][next_pos] + trace_B:
        print(1)
        trace(next_pos, B)
    else:
        print(2)
        trace(A, next_pos)
    return

print(get_shortest_dist(0, 1))
trace(0, 1)

# for d in DP:
#     print(d)