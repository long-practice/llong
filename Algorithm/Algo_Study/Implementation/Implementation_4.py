# 게임 개발

# 풀이방법
# 전형적인 시뮬레이션 문제로 주어진 움직임 방식대로 구현하면 됨
# 1. 현재 위치 기준으로 방향을 틀어 차례대로 갈 곳을 정하기
# 2. 아직 가보지 않은 칸이 존재할 경우 전진, 없다면 회전만 수행
# 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 된 경우 한 칸 뒤로 후진

# 풀이
# 맵 크기: N(세로) x M(가로)
N, M = map(int, input().split(' '))

# 초기 위치: (A, B)
# 방향 d = 0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽
A, B, d = map(int, input().split(' '))

# map에 있는 원소 0: 육지, 1은 바다
map = [list(map(int, input().split(' '))) for n in range(N)]

# map 외부는 바다로 판정하기 때문에 맵 밖으로 1을 도핑해야하나
# 입력 상에서 외곽은 항상 바다로 주어지기 때문에 도핑을 하지 않음

# 현재 위치에서 이동 가능여부 확인
def can_move(A, B, map):
    return map[A - 1][B] == 0 or map[A][B - 1] == 0 or map[A + 1][B] == 0 or map[A][B + 1] == 0

answer = 0

# 3. 현재 위치에서 네 방향 모두 이미 가본 칸 혹은 바다일 경우 이동 종료
while can_move(A, B, map):
    # 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향으로 틀기
    d = (d - 1) % 4

    # 2. 아직 가보지 않은 칸이 존재할 경우 전진, 없다면 회전만 수행
    # 북쪽을 바라본 경우 현재 위치기준 위 칸으로 이동이 가능한지 여부 확인
    if d == 0:
        if map[A - 1][B] == 0:
            # 방문처리
            map[A][B] = 1
            # 현재 위치에서 이동
            A = A - 1
            answer += 1
        continue
    # 동쪽을 바라본 경우
    elif d == 1:
        if map[A][B + 1] == 0:
            map[A][B] = 1
            B = B + 1
            answer += 1
        continue
    # 남쪽을 바라본 경우
    elif d == 2:
        if map[A + 1][B] == 0:
            map[A][B] = 1
            A = A + 1
            answer += 1
        continue
    # 서쪽을 바라본 경우
    elif d == 3:
        if map[A][B - 1] == 0:
            map[A][B] = 1
            B = B - 1
            answer += 1
        continue

# 마지막 현재있는 칸 방문처리
map[A][B] = 1
answer += 1

print(answer)