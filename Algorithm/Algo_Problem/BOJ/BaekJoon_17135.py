# 캐슬 디펜스

# step1 문제상황 구현
# step2 궁수 배치 m C 3
# step3 각 궁수에 대하여 공격 타깃 설정
# function  궁수가 쏠 수 있는 거리에 따라 좌측, 전방, 우측 순으로 탐색하여 해당 차례에 공격할 적 탐색하는 함수
# step4 피격된 적은 게임에서 제외, answer += 1
# step5 위에서 한칸 내려오기 대신 궁수가 한칸 전진함과 동시에 해당 행은 0으로 도핑 / 이후 반복

# step1
# 입력받은 데이터를 이용하여 문제상황 구현
import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip('\n')

N, M, D = map(int, input().split(' '))

original_castle = [list(map(int, input().split(' '))) for _ in range(N)]

# 적이 얼마나 전진해야 field가 0이 될까??
# 궁수가 화살을 쏘는 횟수를 정함으로써 불필요한 반복을 사전에 제한하기 위함
# field위에 적이 얼마나 있는지도 카운팅
iteration, max_enemy = N, 0
counting_enemy = False
for i, row in enumerate(original_castle):
    if 1 in row:
        counting_enemy = True
    if counting_enemy:
        max_enemy += row.count(1)
    else:
        iteration -= 1

# 궁수가 최초에 위치하는 행을 추가
original_castle.append([0 for _ in range(M)])
ans = 0

# function
# 쏠 수 있는 적을 탐색
# 최초 거리 1부터 D까지 궁수 위치(row, col) 기준
# (row, col - 1), (row - 1, col), (row, col + 1)
# (row, col - 2), (row - 1, col - 1), (row - 2, col), (row - 1, col + 1), (row, col + 2) ...
# 위의 순으로 각 칸을 탐색
def func(castle, row, col):
    for dist in range(1, D + 1):
        for dc in range(-dist, dist + 1):
            dr = abs(dc) - dist
            nr, nc = row + dr, col + dc
            if 0 <= nr and 0 <= nc < M and castle[nr][nc] == 1:
                return True, (nr, nc)
    return False, ()

# step2
# 궁수가 위치할 수 있는 칸 생성 후 배치
at_archer = [(N, i) for i in range(M)]

for archer_locs in combinations(at_archer, 3):
    castle = [row[:] for row in original_castle]
    answer = 0

    # step 3
    # iteration 만큼 적이 전진(혹은 궁수가 전진)하게 되면 공격할 수 있는 적이 없음
    # func(castle, archer[0] - i, archer[1])
    # 자동적으로 반복문이 수행되면서 궁수가 전진하는 모습
    for i in range(iteration):
        enemies = set()
        for archer in archer_locs:
            can_attack, enemy = func(castle, archer[0] - i, archer[1])
            if can_attack:
                enemies.add(enemy)

        # step 4
        for enemy in enemies:
            r, c = enemy
            answer += 1
            castle[r][c] = 0

        # step 5
        # 궁수가 전진하면서 해당 행에 있는 모든 원소들을 0으로 처리
        # 1이 남아있게 된다면 function에서 궁수 위치 좌우측에 있는 1을 적으로 감지하게 됨
        for m in range(M):
            castle[N - 1 - i][m] = 0

    if ans < answer:
        ans = answer
        # 완전 탐색 도중 field위의 있는 모든 적을 잡을 수 있었다면 즉시 최댓값 반환 탐색 중지
        if ans == max_enemy:
            break

print(ans)