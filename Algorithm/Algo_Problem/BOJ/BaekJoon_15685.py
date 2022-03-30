# 드래곤 커브

import sys
input = sys.stdin.readline

N = int(input().rstrip())
dragons = [list(map(int, input().rstrip().split())) for _ in range(N)]

visited = [[False for _ in range(101)] for _ in range(101)]
directions = {0: (1, 0), 1: (0, -1), 2: (-1, 0), 3: (0, 1)}

for dragon in dragons:
    x, y, d, g = dragon

    visited[x][y] = True
    x, y = x + directions[d][0], y + directions[d][1]
    visited[x][y] = True

    # 드래곤 이동경로 도출 및 방문처리
    path = [d]
    for _ in range(g):
        for i in range(len(path) - 1, -1, -1):
            direction = (path[i] + 1) % 4
            path.append(direction)
            x, y = x + directions[direction][0], y + directions[direction][1]
            visited[x][y] = True

# 답 도출
answer = 0
for x in range(100):
    for y in range(100):
        if visited[x][y] and visited[x + 1][y] and visited[x][y + 1] and visited[x + 1][y + 1]:
            answer += 1
print(answer)