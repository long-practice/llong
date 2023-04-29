from collections import deque
N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(list(input()))
q = deque()
q.append((0, 0, 1, 0))

visited = [[[False, False] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = True

answer = -1
while q:
    r, c, path, count = q.popleft()
    if r == N - 1 and c == M - 1:
        answer = path
        break

    for nr, nc in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] == '0' and not visited[nr][nc][count]:
                visited[nr][nc][count] = True
                q.append((nr, nc, path + 1, count))
            elif count == 1:
                continue
            elif not visited[nr][nc][1]:
                visited[nr][nc][1] = True
                q.append((nr, nc, path + 1, 1))

print(answer)
