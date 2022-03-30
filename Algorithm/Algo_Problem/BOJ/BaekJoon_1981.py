# 배열에서 이동

# 풀이방법
# 최대값과 최소값의 차이를 mid값으로 이분탐색
# 배열 내 최소값부터 최대값 - mid(이 값을 i)까지 i + mid 까지 배열에 있는 수들에 대해서만 bfs 진행
# 만약 bfs결과 (n, n)까지 도달했다면 mid값을 줄여서 진행

import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
array = []
min_v, Max_v = 200, 0
for _ in range(n):
    a = list(map(int, input().rstrip().split()))
    min_v, Max_v = min(min_v, min(a)), max(Max_v, max(a))
    array.append(a)

def bfs(dif):
    for i in range(min_v, Max_v - dif + 1):
        # 출발칸 뿐만아니라 도착칸도 범위 내에 없으면 bfs를 할 필요가 없음(시간 단축에 중요한 조건)
        if i <= array[0][0] <= i + dif and i <= array[n - 1][n - 1] <= i + dif:
            q = deque([(0, 0)])
            visited = [[False for _ in range(n)] for _ in range(n)]
            visited[0][0] = True

            # 상, 하, 좌, 우 4가지 경우를 풀어쓰므로써 불필요한 조건 판단 제외
            while q:
                r, c = q.popleft()
                if r + 1 < n and not visited[r + 1][c]:
                    if i <= array[r + 1][c] <= i + dif:
                        if r + 1 == n - 1 and c == n - 1:
                            return True
                        visited[r + 1][c] = True
                        q.append((r + 1, c))
                if r - 1 >= 0 and not visited[r - 1][c]:
                    if i <= array[r - 1][c] <= i + dif:
                        visited[r - 1][c] = True
                        q.append((r - 1, c))
                if c + 1 < n and not visited[r][c + 1]:
                    if i <= array[r][c + 1] <= i + dif:
                        if c + 1 == n - 1 and c == r - 1:
                            return True
                        visited[r][c + 1] = True
                        q.append((r, c + 1))
                if c - 1 >= 0 and not visited[r][c - 1]:
                    if i <= array[r][c - 1] <= i + dif:
                        visited[r][c - 1] = True
                        q.append((r, c - 1))
    return False


left, right = 0, Max_v - min_v
while left < right:
    mid = (left + right) >> 1
    possible = bfs(mid)

    # left < right
    # right = mid로 하여 마지막에 불필요한 bfs를 하지 않음으로써 시간 단축
    if possible:
        right = mid
    else:
        left = mid + 1

print(right)