# 버스노선

# 우선 원형을 직선이라고 가정하고 포함관계 확인
# 1. 출발 지점을 오름차순으로 정렬, 도착 지점은 내림차순으로 정렬
# 2. 만약 이전 원소의 도착 지점이 현재 원소의 도착 지점보다 크다면 현재 원소(노선)는 운행 중단
# 3. 모든 원소에 대해 실시
# 4. 원점을 지나는 노선에 대해서(ex. 8 ~ 3) 제일 앞쪽에 있는 원소들에 대해 포함관계 확인

import sys
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
is_operated = [1 for _ in range(M)]
line = []

# 노선을 입력할 때 원점을 지나는 노선들은 종점에 +N을 하여 구분지어 줌
for i in range(1, M + 1):
    x, y = map(int,input().rstrip().split(' '))
    if x < y:
        line.append([x, y, i])
    else:
        line.append([x, y + N, i])
line.sort(key = lambda x: [x[0], -x[1]])

prev_a, prev_b, prev_c = 0, 0, 0
for l in line:
    a, b, c = l
    if a > b:
        b += N
    if b <= prev_b:
        is_operated[c - 1] = 0
    else:
        prev_a, prev_b, prev_c = a, b, c

if prev_b > N:
    prev_b -= N
    for l in line:
        if l[0] >= prev_b:
            break
        if is_operated[l[2] - 1] and l[0] < l[1]:
            if l[1] <= prev_b:
                is_operated[l[2] - 1] = 0

print(*[i for i, x in enumerate(is_operated, start = 1) if x])