# 2번
# 준겸이는 N X M칸으로 이루어진 도넛 모양의 행성에 살고 있다.
# 준겸이가 살고 있는 행성에는 위 그림처럼 격자 모양으로 줄이 그어져 있다.
# 행성의 각 칸은 숲으로 막혀 있거나, 지나갈 수 있도록 비어 있다.
#
# 준겸이는 본인의 집이 있는 위치를 기준으로 삼아 (0,0)이라고 표시하기로 했다.
# 준겸이는 행성 위에서 상하좌우로 걸어 다닐 수 있다. 준겸이가 오른쪽으로 한 칸 걸어가면, 위치 (0,1)에 도달할 것이다.
# 마찬가지로 아래로 한 칸 걸어가면, 위치 (1,0)에 도달할 것이다.
# 준겸이가 (0,0)에서 M칸 오른쪽으로 걸어가면, 한 바퀴를 돌아 다시 원래 자리로 되돌아오게 된다.
# 비슷하게 (0,0)에서 N칸 아래로 걸어가면, (0,0)으로 돌아오게 된다.
#
# 행성은 연결되어 있기 때문에, 준겸이가 (0,0)에서 왼쪽으로 한 칸 걸어가면 위치 (0,M-1)에 도달할 것이다.
# 마찬가지로 준겸이가 (0,0)에서 위로 한 칸 걸어가면 (N-1, 0)에 도달하게 된다.
#
# 준겸이는 행성을 탐험하려고 한다. 만약 준겸이가 비어 있는 어떤 칸 A=(p_1,q_1)에서 시작해,
# 숲에 막히지 않고 비어 있는 칸 B=(p_2,q_2)에 도달할 수 있다면 A와 B는 같은 구역이다.
# 반대로, 도달할 수 없다면 A와 B는 서로 다른 구역이다. 당신은 준겸이가 탐험할 수 있는 빈 구역의 개수가 몇 개인지 출력해야 한다.

# 5 6
# 1 1 1 1 1 1
# 1 0 0 0 1 1
# 1 1 1 1 0 0
# 1 1 1 1 0 0
# 1 1 1 1 1 1
# answer: 2

# 7 8
# 0 0 1 1 0 0 0 0
# 0 1 1 1 1 0 1 0
# 1 1 1 1 1 1 1 1
# 0 1 1 1 1 1 0 0
# 1 1 0 0 0 1 0 0
# 0 1 0 0 0 1 0 1
# 0 0 1 1 1 1 0 0
# answer: 2

import sys
input = sys.stdin.readline

from collections import deque

N, M = map(int, input().rstrip().split())
planet = [list(map(int, input().rstrip().split())) for _ in range(N)]

def dfs(r, c):
    planet[r][c] = 1
    for nr, nc in [((r + 1) % N, c), ((r - 1) % N, c), (r, (c + 1) % M), (r, (c - 1) % M)]:
        if not planet[nr][nc]:
            dfs(nr, nc)
    return 1

def bfs(row, col):
    q = deque([(row, col)])
    while q:
        r, c = q.popleft()
        for nr, nc in [((r + 1) % N, c), ((r - 1) % N, c), (r, (c + 1) % M), (r, (c - 1) % M)]:
            if not planet[nr][nc]:
                planet[nr][nc] = 1
                q.append((nr, nc))
    return 1


answer = 0
for row in range(N):
    for col in range(M):
        if not planet[row][col]:
            answer += bfs(row, col)

print(answer)
