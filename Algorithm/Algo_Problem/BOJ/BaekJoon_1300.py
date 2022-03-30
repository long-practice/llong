# K번째 수

# 풀이방법
# 제한 조건에 따르면 N 은 10 ** 5보다 작거나 같은 자연수이기 때문에
# 배열을 생성하고 각 행을 이어붙여서 정렬을 할 시 시간복잡도 O(nlog(n))이므로 시간초과가 됨
# 또한 정답을 1부터 10 ** 10 까지의 수로 순차 탐색을 할 경우에도 시간초과가 나게 되므로
# 반드시 이분탐색을 이용해야 함

# 결정문제로 환원
# 만약 정답이 x일 때
# x보다 작은 수의 값이 몇 개인가? n개
# n이 k보다 작은가? 큰 가?에 따라서 left, right값을 조정하여 문제 해결

import sys
input = sys.stdin.readline

N = int(input())
k = int(input())


def get_count_under(x):
    res = 0
    l, r = 1, N + 1
    # x보다 작은 값이 아예 없는 행이 어디서부터 시작되는지 이분탐색을 적용하여 탐색
    while l <= r:
        m = (l + r) >> 1
        if x // m == 0:
            r = m - 1
        else:
            l = m + 1

    # 해당행 바로 위에서부터 x보다 작은 값이 존재하므로
    # 행에서 모든 값이 x보다 작게되는 행부터 그 위로는 모두 N개
    r = min(r, N)
    for row in range(r, 0, -1):
        v = x // row
        if v < N:
            res += v
        else:
            res += row * N
            break
    return res


left, right = 0, N * N
while left <= right:
    mid = (left + right) >> 1
    if get_count_under(mid) >= k:
        right = mid - 1
    else:
        left = mid + 1

print(left)