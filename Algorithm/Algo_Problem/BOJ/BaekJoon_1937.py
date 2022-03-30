# 욕심쟁이 판다

# 풀이방법
# 배열 내 모든 원소에 대해 방문할 수 있는 칸(흐름)이 매순간 똑같으므로 메모이제이션기법을 이용하여 같은 계산을 방지
# 모든 원소에 대해 dfs를 진행하되 방문한 칸에 대해서는 이전 계산값을 불러와서 반복되는 계산을 방지
# 1520. 내리막길과 유사한 문제

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4))

n = int(input().rstrip())
array = [list(map(int, input().rstrip().split(' '))) for _ in range(n)]
DP = [[0 for _ in range(n)] for _ in range(n)]


def dfs(row, col):
    if not DP[row][col]:
        DP[row][col] = 1
        if 0 <= row - 1 and array[row][col] < array[row - 1][col]:
            DP[row][col] = max(dfs(row - 1, col) + 1, DP[row][col])
        if row + 1 < n and array[row][col] < array[row + 1][col]:
            DP[row][col] = max(dfs(row + 1, col) + 1, DP[row][col])
        if 0 <= col - 1 and array[row][col] < array[row][col - 1]:
            DP[row][col] = max(dfs(row, col - 1) + 1, DP[row][col])
        if col + 1 < n and array[row][col] < array[row][col + 1]:
            DP[row][col] = max(dfs(row, col + 1) + 1, DP[row][col])
    return DP[row][col]


answer = 0
for r in range(n):
    for c in range(n):
        answer = max(answer, dfs(r, c))
print(answer)