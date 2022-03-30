# 다리 만들기 2

# 풀이방법
# 1. 입력구현
# 2. dfs를 이용하여 각각의 땅들에 대해 0 ~ n의 숫자로 표현(grouping)
# 3. 가장자리 땅에서 가로 혹은 세로로 다리를 놓았을 때 어느 땅과 얼마만큼의 길이로 연결가능한지 인접 행렬로 표기
# 4. 크루스칼 알고리즘으로 최소 신장트리 구성
# 5. 예외처리

import heapq
import sys
input = sys.stdin.readline

# 1. 입력구현
N, M = map(int, input().rstrip().split())
board = [list(map(int, input().rstrip().split())) for _ in range(N)]

# for b in board:
#     print(b)

# 2. dfs를 이용하여 각각의 땅들에 대해 0 ~ n의 숫자로 표현(grouping)
visited = [[False for _ in range(M)] for _ in range(N)]
def dfs(row, col, count):
    visited[row][col] = True
    board[row][col] = count

    if row + 1 < N and board[row + 1][col] and not visited[row + 1][col]:
        dfs(row + 1, col, count)
    if row - 1 >= 0 and board[row - 1][col] and not visited[row - 1][col]:
        dfs(row - 1, col, count)
    if col + 1 < M and board[row][col + 1] and not visited[row][col + 1]:
        dfs(row, col + 1, count)
    if col - 1 >= 0 and board[row][col - 1] and not visited[row][col - 1]:
        dfs(row, col - 1, count)


n = 1
for r in range(N):
    for c in range(M):
        if not visited[r][c] and board[r][c]:
            dfs(r, c, n)
            n += 1

# n - 1: 섬의 개수
# for b in board:
#     print(b)
# print()

# 3. 가장자리 땅에서 가로 혹은 세로로 다리를 놓았을 때 어느 땅과 얼마만큼의 길이로 연결가능한지 간선정보 표현
INF = 100
vertax = []

def get_hor_distance(row, col):
    for curr_c in range(col + 1, M):
        if board[row][curr_c]:
            return abs(curr_c - col) - 1, board[row][curr_c]
    return INF, 0

def get_ver_distance(row, col):
    for curr_r in range(row + 1, N):
        if board[curr_r][col]:
            return abs(curr_r - row) - 1, board[curr_r][col]
    return INF, 0

for r in range(N):
    for c in range(M):
        dep = board[r][c]
        if dep:
            if c + 1 < M - 2 and not board[r][c + 1]:
                dist, arr = get_hor_distance(r, c)
                if 1 < dist < INF:
                    heapq.heappush(vertax, (dist, dep, arr))
            if r + 1 < N - 2 and not board[r + 1][c]:
                dist, arr = get_ver_distance(r, c)
                if 1 < dist < INF:
                    heapq.heappush(vertax, (dist, dep, arr))
# print(vertax)

# 4. 크루스칼 알고리즘으로 최소 신장트리 구성
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    A, B = find(a), find(b)
    parent[max(A, B)] = min(A, B)

parent = [i for i in range(n)]
answer, select_v = 0, 0
while vertax:
    cost, a, b = heapq.heappop(vertax)

    if find(a) != find(b):
        union(a, b)
        answer += cost
        select_v += 1

    # 5. 예외처리
    if select_v == n - 2:
        print(answer)
        exit(0)
print(-1)