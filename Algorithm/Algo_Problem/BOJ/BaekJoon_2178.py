# 미로 탐색
from itertools import islice
from collections import deque

def bfs(maze, row, col, count):
    queue = deque()
    queue.append((row, col))

    while queue:
        r, c = queue.popleft()
        if r == N and c == M:
            break
        if maze[r + 1][c] == 1:
            maze[r + 1][c] += maze[r][c]
            queue.append((r + 1, c))
        if maze[r - 1][c] == 1:
            maze[r - 1][c] += maze[r][c]
            queue.append((r - 1, c))
        if maze[r][c + 1] == 1:
            maze[r][c + 1] += maze[r][c]
            queue.append((r, c + 1))
        if maze[r][c - 1] == 1:
            maze[r][c - 1] += maze[r][c]
            queue.append((r, c - 1))

    return maze[r][c]

N, M = map(int, input().split(' '))
temp_maze = [list(map(int, islice(input(), M))) for _ in range(N)]

maze = [[0 for _ in range(M + 2)] for _ in range(N + 2)]

for r in range(N):
    for c in range(M):
        maze[r + 1][c + 1] = temp_maze[r][c]

print(bfs(maze, 1, 1, 1))