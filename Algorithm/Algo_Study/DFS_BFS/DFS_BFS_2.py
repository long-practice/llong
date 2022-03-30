# 미로탈출

# 해결방법
# 처음 위치에 대해 BFS 적용
# 1인 위치에 대해 현재까지 이동한 칸의 수로 값을 초기화
# 마지막 목표 지점에 도달 했을 때의 움직인 칸을 구해내기

# 예시
# 5 6
# 101010 > 1번째 (1)
# 111111 > 1번째 ~ 6번째 (2 ~ 7)
# 000001 > 6번째 (8)
# 111111 > 6번째 (9)
# 111111 > 6번째 (10)

# 3 3
# 110 > 1 ~ 2번째(1 ~ 2)
# 010 > 2번째(3)
# 011 > 2 ~ 3번째(4 ~ 5)

# 풀이
from collections import deque

# 시작 위치를 큐에 넣은 상태로 큐를 생성
# 위, 아래, 양 옆에 있는 값들을 확인하고
# 만약 그 값이 1이라면 다음 경로로 선택, 큐에 삽입, 해당 칸의 값은 지나온 칸의 개수 만큼 초기화
# 큐에 다음으로 이동할 경로가 없어질 때까지 반복
# maze_map[N][M]에 해당하는 값이 (N, M)까지 이동하는데 지나온 칸의 개수
def BFS(node):
    queue = deque([node])
    dr = [0, 0, -1, 1]
    dc = [-1, 1, 0, 0]

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            if maze_map[r + dr[i]][c + dc[i]] == 1:
                maze_map[r + dr[i]][c + dc[i]] += maze_map[r][c]
                next = (r + dr[i], c + dc[i])
                queue.append(next)

    return maze_map[N][M]


# N(행) X M(열) 2차원 리스트 생성
N, M = map(int, input().split(' '))

# 주어진 입력에 따라 미로 생성 및 외곽 0으로 도핑
maze = [list(map(int, input())) for _ in range(N)]
maze_map = [[0 for _ in range(M + 2)] for _ in range(N + 2)]

for n in range(1, N + 1):
    for m in range(1, M + 1):
        maze_map[n][m] = maze[n - 1][m - 1]

start = (1, 1)
answer = BFS(start)

print(answer)
