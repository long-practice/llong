# LIS

# 이분탐색을 이용한 정답수열을 도출하는 문제
# 각각의 원소들에 대해 bisect_left를 했을 때 구해지는 인덱스를 따로 LIS_idx 리스트에 저장
# 이 후 기존 방식과 동일하게 역추적하여 정답수열 도출
# 아래 코드는 가장 큰 증가 부분 수열(이분탐색 이용)의 정답 수열을 출력(14003번 문제)
# 이분탐색 방식, 역추적 방식은 암기해둘 것
import sys
from bisect import bisect_left

input = sys.stdin.readline
N = int(input().rstrip())
A = list(map(int, input().rstrip().split(' ')))
LIS = [int(1e9)]
LIS_idx = []

for a in A:
    if LIS[-1] < a:
        LIS.append(a)
        LIS_idx.append(len(LIS))
    else:
        i = bisect_left(LIS, a)
        LIS[i] = a
        LIS_idx.append(i + 1)

count = len(LIS)
print(count)
i = 1
answer = []
while count > 0:
    if LIS_idx[-i] == count:
        answer.append(A[-i])
        count -= 1
    i += 1
print(*answer[::-1])

