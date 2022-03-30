# 왕실의 나이트

# 풀이 방법
# 한 위치에서 이동할 수 있는 경우의 수 8가지에 대해서
# 이동한 위치가 체스판 위에 있는 경우를 세어내면 됨
# 움직임을 표현하기 위해서 선형배열 이용

# 예시
# 현재 위치가 a1이라면
# 이동할 수 있는 위치는 b3, c2 2가지

# 현재 위치가 c2라면
# 이동할 수 있는 위치는 a1, a3, b4, d4, e3, e1 6가지

# 풀이
# 현재 위치 입력받기
# loc_x, loc_y의 가능한 최솟값은 1 최댓값은 8
loc = input()
loc_x = ord(loc[0]) - ord('a') + 1
loc_y = int(loc[1])
loc_max = 8

# 나이트의 움직임을 선형배열로 표현
dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [1, -1, 2, -2, 2, -2, 1, -1]

answer = 0

# 8가지 움직임 이후 체스판 안에 나이트가 존재하는지 확인
for i in range(8):
    curr_x = loc_x + dx[i]
    curr_y = loc_y + dy[i]
    if 1 <= curr_x <= loc_max and 1 <= curr_y <= loc_max:
        answer += 1
print(answer)