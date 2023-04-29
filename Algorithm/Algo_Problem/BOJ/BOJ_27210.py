# 1번
# 신을 모시는 사당에는 신을 조각한 돌상 N개가 일렬로 놓여 있다.
# 각 돌상은 왼쪽 또는 오른쪽을 바라보고 서있다. 창영이는 연속한 몇 개의 돌상에 금칠을 하여 궁극의 깨달음을 얻고자 한다.
#
# 궁극의 깨달음을 얻기 위해서는 가능한 한 많은 금색 돌상들이 같은 방향을 바라보아야 한다. 방향이 다른 돌상은 깨달음에 치명적이다.
# 깨달음의 양은 아래와 같이 정의된다.
# | (왼쪽을 바라보는 금색 돌상의 개수) - (오른쪽을 바라보는 금색 돌상의 개수) |
#
# 창영이는 궁극의 깨달음을 얻을 수 있을까?(최대로 얻을 수 있는 깨달음 구하기)

# 5
# 1 1 2 1 2
# answer: 2

# 1
# 1
# answer: 1

# 2
# 1 2
# answer: 1


import sys
input = sys.stdin.readline

N = int(input().rstrip())
ls = list(map(int, input().rstrip().split()))

table = [[0 for _ in range(N)] for _ in range(2)]
table[ls[0] - 1][0] = 1

for i in range(1, N):
    c = ls[i] - 1
    table[c][i] = max(1, table[c][i - 1] + 1)
    table[c ^ 1][i] = max(0, table[c ^ 1][i - 1] - 1)

answer = 0
for i in range(N):
    for j in range(2):
        answer = max(answer, table[j][i])

print(answer)
