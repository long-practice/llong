# 배열 돌리기 4
import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split())
array = [list(map(int, input().rstrip().split())) for _ in range(N)]
rotations = [tuple(map(int, input().rstrip().split())) for _ in range(K)]


def rotate(r, c, t, A):
    res = [row[:] for row in A]
    for s in range(1, t + 1):
        temp = res[r - s][c - s]
        for k in range(2 * s):
            res[r - s + k][c - s] = res[r - s + k + 1][c - s]
        for k in range(2 * s):
            res[r + s][c - s + k] = res[r + s][c - s + k + 1]
        for k in range(2 * s):
            res[r + s - k][c + s] = res[r + s - k - 1][c + s]
        for k in range(2 * s):
            res[r - s][c + s - k] = res[r - s][c + s - k - 1]
        res[r - s][c - s + 1] = temp
    return res


def backtracking(L, mat):
    global answer
    if L == K:
        answer = min(answer, min([sum(row) for row in mat]))
        return
    else:
        for i in range(K):
            if not check[i]:
                check[i] = True
                backtracking(L + 1, rotate(rotations[i][0] - 1, rotations[i][1] - 1, rotations[i][2], mat))
                check[i] = False
        return

answer = int(1e4)
check = [False for _ in range(K)]

backtracking(0, array)
print(answer)