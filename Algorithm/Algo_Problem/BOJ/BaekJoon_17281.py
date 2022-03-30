# 야구

# 선수들의 타순이 나올 경우의수 8! = 40320
# 40320가지의 순열에 대해 모든 점수의 경우의 수를 파악
from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input().rstrip())
innings = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]

def count_score(init):
    global score
    # base_1: 1루 base_2: 2루 base_3: 3루
    base_1, base_2, base_3 = 0, 0, 0
    out = 0
    for i in range(init, 40):
        v = inning[seq[i % 9]]
        if v:
            # 안타
            if v == 1:
                score += base_3
                base_1, base_2, base_3 = 1, base_1, base_2
            # 1루타
            elif v == 2:
                score += base_2 + base_3
                base_1, base_2, base_3 = 0, 1, base_1
            # 2루타
            elif v == 3:
                score += base_1 + base_2 + base_3
                base_1, base_2, base_3 = 0, 0, 1
            # 3루타
            else:
                score += base_1 + base_2 + base_3 + 1
                base_1, base_2, base_3 = 0, 0, 0
        else:
            # aut
            out += 1
            if out == 3:
                # 다음 타자 반환
                return (i + 1) % 9

answer = 0
for seq in permutations([x for x in range(1, 9)]):
    seq = list(seq)
    # 1번 선수 4번 타자 고정
    seq = seq[:3] + [0] + seq[3:]
    # 최초 1번 타자 설정
    s = 0
    score = 0
    for inning in innings:
        s = count_score(s)
    answer = max(answer, score)

print(answer)