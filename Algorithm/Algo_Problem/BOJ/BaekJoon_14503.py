# 로봇 청소기

import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
r, c, d = map(int, input().rstrip().split())
array = [list(map(int, input().rstrip().split())) for _ in range(N)]
# 북 동 남 서
direction = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}

def clear_left(row, col, d):
    dr, dc = direction[d]
    if array[row + dr][col + dc] == 0:
        return False
    else:
        return True

answer = 0
while True:
    if array[r][c] == 0:
        answer += 1
    print(r, c, d)
    array[r][c] = 2
    for _ in range(4):
        if not clear_left(r, c, (d - 1) % 4):
            d = (d - 1) % 4
            r += direction[d][0]
            c += direction[d][1]
            break
        else:
            d = (d - 1) % 4
    else:
        if array[r - direction[d][0]][c - direction[d][1]] != 1:
            r -= direction[d][0]
            c -= direction[d][1]
        else:
            break
    # for arr in array:
    #     print(arr)
    # print()
print(answer)