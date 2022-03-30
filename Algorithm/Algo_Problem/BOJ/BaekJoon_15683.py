# 감시
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split(' '))
office = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]

# (행, 열, 종류)
cctv = []
wall = 0


for r in range(N):
    for c in range(M):
        if 0 < office[r][c] < 6:
            cctv.append((r, c, office[r][c]))
        elif office[r][c] == 6:
            wall += 1

# 각 cctv에 대해 볼 수 있는 구역을 리스트로 표현
cctv_can_see = {x: [] for x in range(len(cctv))}

# 해당 행, 열이 벽인지 아닌지 판단
def is_wall(row, col):
    return office[row][col] == 6


# 오른쪽으로 관제 가능한 구역
def see_right(row, col):
    can_see = []
    for c in range(col + 1, M):
        if not is_wall(row, c):
            can_see.append((row, c))
        else:
            break
    return can_see

# 왼쪽으로 관제 가능한 구역
def see_left(row, col):
    can_see = []
    for c in range(col - 1, -1, -1):
        if not is_wall(row, c):
            can_see.append((row, c))
        else:
            break
    return can_see

# 위쪽으로 관제 가능한 구역
def see_up(row, col):
    can_see = []
    for r in range(row - 1, -1, -1):
        if not is_wall(r, col):
            can_see.append((r, col))
        else:
            break
    return can_see

# 아래쪽으로 관제 가능한 구역
def see_down(row, col):
    can_see = []
    for r in range(row + 1, N):
        if not is_wall(r, col):
            can_see.append((r, col))
        else:
            break
    return can_see

# 1번 카메라 동작 구현
def oper_first_cctv(row, col):
    res = []
    res.append(see_right(row, col))
    res.append(see_left(row, col))
    res.append(see_up(row, col))
    res.append(see_down(row, col))
    return res

# 2번 카메라 동작구현
def oper_second_cctv(row, col):
    res = []
    res.append(see_right(row, col) + see_left(row, col))
    res.append(see_up(row, col) + see_down(row, col))
    return res

# 3번 카메라 동작구현
def oper_third_cctv(row, col):
    l, r, u, d = see_left(row, col), see_right(row, col), see_up(row, col), see_down(row, col)
    res = []
    res.append(r + d)
    res.append(d + l)
    res.append(l + u)
    res.append(u + r)
    return res

# 4번 카메라 동작구현
def oper_fourth_cctv(row, col):
    l, r, u, d = see_left(row, col), see_right(row, col), see_up(row, col), see_down(row, col)
    res = []
    res.append(r + d + l)
    res.append(d + l + u)
    res.append(l + u + r)
    res.append(u + r + d)
    return res

# 5번 카메라 동작구현
def oper_fifth_cctv(row, col):
    res = []
    res.append(see_left(row, col) + see_right(row, col) + see_up(row, col) + see_down(row, col))
    return res

# 각각의 cctv 설치방법에 따라 관제할 수 있는 칸들이 다르므로
# 백트래킹을 이용하여 관제할 수 있는 칸들을 cctv당 하나씩 선택하여
# 최종적으로 관제할 수 있는 구역을 전체 칸에서 빼줌
def back_tracking(i, res):
    global answer
    if i == len(cctv):
        answer = min(answer, N * M - wall - len(set(res)))
        return
    else:
        for a in cctv_can_see[i]:
            back_tracking(i + 1, res + a)

answer = 65
for i, cam in enumerate(cctv):
    if cam[2] == 1:
        cctv_can_see[i] = oper_first_cctv(cam[0], cam[1])
    elif cam[2] == 2:
        cctv_can_see[i] = oper_second_cctv(cam[0], cam[1])
    elif cam[2] == 3:
        cctv_can_see[i] = oper_third_cctv(cam[0], cam[1])
    elif cam[2] == 4:
        cctv_can_see[i] = oper_fourth_cctv(cam[0], cam[1])
    else: # cam[2] == 5:
        cctv_can_see[i] = oper_fifth_cctv(cam[0], cam[1])

back_tracking(0, [(x, y) for x, y, _ in cctv])
print(answer)