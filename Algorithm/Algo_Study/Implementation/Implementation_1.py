# 상하좌우

# 풀이방법
# 대표적인 시뮬레이션 문제 중 하나
# 최초 위치(1, 1)에서 L, R, U, D를 인식할 때마다 움직임 구현
# 각 움직임을 선형 배열을 이용하여 표현, 단순화하여 문제 해결

# 예시
# L: 왼쪽으로 한 칸 이동(dx = -1)
# R: 오른쪽으로 한 칸 이동(dx = 1)
# U: 위쪽로 한 칸 이동(dy = -1)
# D: 아래쪽으로 한 칸 이동(dy = 1)

# 풀이
N = int(input())

plans = input().split(' ')

# 좌표가 (row, column)인 것에 유의
# dx, dy는 각각 dc, dr로 표현
r, c = 1, 1
dr = [-1, 1]
dc = [-1, 1]

# 각각의 움직임 구현
# 움직일 수 있는 조건(지도 밖을 벗어나지 않는 조건)을 잘 파악할 것
for plan in plans:
    if plan == 'L' and c > 1:
        c += dc[0]
    elif plan == 'R' and c < N:
        c += dc[1]
    elif plan == 'U' and r > 1:
        r += dr[0]
    elif plan == 'D' and r < N:
        r += dr[1]

print(r, c)