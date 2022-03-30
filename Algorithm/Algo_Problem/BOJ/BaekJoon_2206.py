# 벽 부수고 이동하기

# 풀이방법
# bfs 이용
# 큐에 현재 행, 열, 이동칸 수, 벽을 한 번 부붰는지 여부를 넣어 나중에 조건판단을 용이하게 함
# 또한 visited를 3차원으로 선언하여 벽을 부수고 이동했을 때, 부수지 않고 이동했을 때 경우를 따로 카운팅시킴

from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))

board = [list(input().rstrip()) for _ in range(N)]
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

    # 기존 dr, dc 리스트를 선언했을 때 보다 우수한 시간 성능을 보임
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