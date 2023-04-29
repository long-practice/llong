import sys
input = sys.stdin.readline

N, M, H = map(int, input().rstrip().split())
ladders = [tuple(map(int, input().rstrip().split())) for _ in range(M)]

board = [[False for _ in range(N + 1)] for _ in range(H + 1)]
for ladder in ladders:
    r, c = ladder
    board[r][c] = True

answer = 4


def well_set():
    res = [i for i in range(N + 1)]
    for r in range(1, H + 1):
        for c in range(1, N):
            if board[r][c]:
                res[c], res[c + 1] = res[c + 1], res[c]
    return res == [i for i in range(N + 1)]


def well_set2():
    for c in range(1, N + 1):
        col_res = c
        for r in range(1, H + 1):
            if board[r][col_res]:
                col_res += 1
            elif board[r][col_res - 1]:
                col_res -= 1
        if col_res != c:
            return False
    return True


def set_ladder(ladder_count, curr_r, curr_c):
    global answer
    if ladder_count >= answer:
        return

    if well_set2():
        answer = min(answer, ladder_count)
    else:
        for row in range(curr_r, H + 1):
            if row != curr_r:
                curr_c = 1
            for col in range(curr_c, N):
                if board[row][col]:
                    col += 1
                elif board[row][col + 1]:
                    col += 2
                else:
                    board[row][col] = True
                    set_ladder(ladder_count + 1, row, col + 2)
                    board[row][col] = False
    return


set_ladder(0, 1, 1)
print(answer if answer < 4 else -1)