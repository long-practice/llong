# 구간 나누기 2

# 이분탐색 이용
# 결정 문제로 환원, 구간 점수를 mid값으로 설정한 후
# 전체 구간을 m개의 구간으로 나눌 수 있는지 확인
# m개 이상의 구간으로 나누어진다면 mid값 수정

import sys
sys.setrecursionlimit(int(1e4))
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))
array = list(map(int, input().rstrip().split(' ')))

left, right = 0, 10000
while left <= right:
    mid = (left + right) // 2
    count = 1

    interval_min, interval_max = 10000, 0
    for a in array:
        interval_min = min(interval_min, a)
        interval_max = max(interval_max, a)

        if interval_max - interval_min > mid:
            count += 1
            interval_max = interval_min = a

        if count > M:
            break

    if count < M:
        right = mid - 1
    else:
        left = mid + 1

print(right)



