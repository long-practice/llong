# 연구소 2

# step1: 입력받기
# func1: two_field 탐색
# step2: two_field에 대해서 M개 선택
# func2: bfs 최단거리 구하는 함수 구현, 만약 바이러스가 퍼질 수 있는 곳에 방문처리가 안됐다면 큰 값(10000)반환
# step3: 모든 two_field에 대해 최단거리를 구했다면 연구소 내에 최댓값을 구해 answer에 append
# step4: 구해진 answer들 중 큰 값만 있으면 바이러스를 모두 퍼뜨릴 수 없으므로 -1 출력, 이 밖의 경우에 대해 최소값 출력

# step1
import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

# 입력
N, M = map(int, input().split(' '))
lab = [list(map(int, input().split(' '))) for _ in range(N)]

# func1
def get_two_fields(lab, N, V):
    two_field = []
    for r in range(0, N):
        for c in range(0, N):
            if lab[r][c] != 1:
                if lab[r][c] == 2:
                    two_field.append((r, c))
                    V -= 1
                V += 1
    return two_field, V

# two_field 탐색, 바이러스가 채워져야할 공간 카운팅
two_fields, V = get_two_fields(lab, N, 0)

# func2
def get_shortest_dist(lab, field, N, V):
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    is_virus = [[False for _ in range(N)] for _ in range(N)]

    queue = deque()
    for r, c in field:
        queue.append((r, c, 0))

    while queue:
        r, c, count = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr <= N - 1 and 0 <= nc <= N - 1:
                if lab[nr][nc] != 1 and not is_virus[nr][nc]:
                    is_virus[nr][nc] = True
                    queue.append((nr, nc, count + 1))
                    if lab[nr][nc] == 0:
                        V -= 1
                        if V == 0:
                            return count + 1
    return 10000

answer = []
# step2
if V != 0:
    for two_field in combinations(two_fields, M):
        # step3
        answer.append(get_shortest_dist(lab, two_field, N, V))

    # step4
    if min(answer) == 10000:
        print(-1)
    else:
        print(min(answer))
else:
    print(0)



def get_shortest_dist(lab, field, N, V):
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]
    queue = deque()
    for r, c in field:
        queue.append((r, c, 0))

    is_virus = [[False for _ in range(N)] for _ in range(N)]
    for r, c in two_fields:
        is_virus[r][c] = True

    while queue:
        if V == 0:
            return count + 1
        r, c, count = queue.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr <= N - 1 and 0 <= nc <= N - 1:
                if lab[nr][nc] == 0 and not is_virus[nr][nc]:
                    is_virus[nr][nc] = True
                    V -= 1
                    queue.append((nr, nc, count + 1))
                elif lab[nr][nc] == 2:
                    queue.append((nr, nc, count + 1))
    return 10000