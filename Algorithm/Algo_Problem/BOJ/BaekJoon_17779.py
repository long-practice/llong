# 게리맨더링 2

# 1, 2, 3, 4 구역을 리스트 슬라이싱을 이용하여 바로바로 계산하는 방법
import sys
input = sys.stdin.readline

# 1. 문제 상황 구현
N = int(input().rstrip())
city = []
total = 0
for _ in range(N):
    row = list(map(int, input().rstrip().split(' ')))
    total += sum(row)
    city.append(row)

answer = 2000

for