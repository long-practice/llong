# 레이저 통신
import sys
input = sys.stdin.readline

import heapq

C, R = map(int, input().rstrip().split())
board = [list(input().rstrip()) for _ in range(R)]
table = [[[int(1e4), int(1e4)] for _ in range(C)] for _ in range(R)]
# table = [[int(1e4) for _ in range(C)] for _ in range(R)]

direction = {'L': 0, 'R': 0, 'U': 1, 'D': 1}
dr_dc = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}

start_end = []
for r in range(R):
    for c in range(C):
        if board[r][c] == 'C':
            start_end.append((r, c))

curr_r, curr_c = start_end[0]

h = []
for d in ['L', 'R', 'U', 'D']:
    cr, cc = start_end[0]

    if 0 <= cr + dr_dc[d][0] < R and 0 <= cc + dr_dc[d][1] < C and board[cr + dr_dc[d][0]][cc + dr_dc[d][1]] != '*':
        nr, nc = cr + dr_dc[d][0], cc + dr_dc[d][1]
        table[nr][nc][direction[d]] = 0
        # table[nr][nc] = 0
        heapq.heappush(h, (0, nr, nc, direction[d]))


while h:
    count, row, col, di = heapq.heappop(h)

    if row == start_end[1][0] and col == start_end[1][1]:
        break

    for d in ['L', 'R', 'U', 'D']:
        if 0 <= row + dr_dc[d][0] < R and 0 <= col + dr_dc[d][1] < C\
                and board[row + dr_dc[d][0]][col + dr_dc[d][1]] != '*':
            nr, nc = row + dr_dc[d][0], col + dr_dc[d][1]
            ncount = count + (di ^ direction[d])

            if table[nr][nc][direction[d]] > ncount:
                table[nr][nc][direction[d]] = ncount
                heapq.heappush(h, (ncount, nr, nc, direction[d]))

print(table[start_end[1][0]][start_end[1][1]])