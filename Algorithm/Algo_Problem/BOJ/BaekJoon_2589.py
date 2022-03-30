import sys
from collections import deque

# 어떤 위치에서 특정 방향 양 옆으로 이동가능하다면 그 위치에는 보물이 위치할 수 없음

def func2(board, point):
    row, col = point
    visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
    queue = deque([(row, col, 0)])
    visited[row][col] = True
    dist = []

    while queue:
        r, c, count = queue.popleft()
        dist.append(count)

        if board[r + 1][c] == 'L' and not visited[r + 1][c]:
            queue.append((r + 1, c, count + 1))
            visited[r + 1][c] = True
        if board[r - 1][c] == 'L' and not visited[r - 1][c]:
            queue.append((r - 1, c, count + 1))
            visited[r - 1][c] = True
        if board[r][c + 1] == 'L' and not visited[r][c + 1]:
            queue.append((r, c + 1, count + 1))
            visited[r][c + 1] = True
        if board[r][c - 1] == 'L' and not visited[r][c - 1]:
            queue.append((r, c - 1, count + 1))
            visited[r][c - 1] = True

    return max(dist)

def cannot_set_treasure(map, row, col):
    return map[row + 1][col] == map[row - 1][col] == 'L' or map[row][col + 1] == map[row][col - 1] == 'L'

row, col = map(int, input().split(' '))
map = [['W' for _ in range(col + 2)] for _ in range(row + 2)]
answer = []

for r in range(1, row + 1):
    arr = sys.stdin.readline().rstrip(' ')
    for c in range(1, col + 1):
        map[r][c] = arr[c - 1]

for r in range(1, row + 1):
    for c in range(1, col + 1):
        if map[r][c] == 'L':
            if not cannot_set_treasure(map, r, c):
                answer.append(func2(map, (r, c)))
print(max(answer))