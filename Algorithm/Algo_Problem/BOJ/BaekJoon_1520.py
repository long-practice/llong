# 내리막길

# DFS, DP 이용하여 현재 위치에서 낮은 위치로 깊이 탐색
# DP[r][c] == -1인 곳은 아직 탐색을 하지 않은 곳으로 -1인 곳에서만 탐색을 진행
# 탐색이 가능한 지점에서만 DFS 진행하여 우측 하단까지 도착하는 경로의 수를 저장
# 따라서 되돌아오면서 DP[r][c] 값은 수정이 되는데, 이 값은 현재위치에서 우측 하단까지 도착하는 경로의 수가 됨.
# 최종적으로 DP[0][0]의 값이 답이 됨
import sys

input = sys.stdin.readline
sys.setrecursionlimit(int(1e4))
row, col = map(int, input().rstrip().split(' '))
array = [list(map(int, input().rstrip().split(' '))) for _ in range(row)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
DP = [[-1 for _ in range(col)] for _ in range(row)]


def search_road(r, c):
    if r == row - 1 and c == col - 1:
        return 1
    if DP[r][c] == -1:
        DP[r][c] += 1
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if 0 <= nr <= row - 1 and 0 <= nc <= col - 1 and array[r][c] > array[nr][nc]:
                DP[r][c] += search_road(nr, nc)
    return DP[r][c]


print(search_road(0, 0))