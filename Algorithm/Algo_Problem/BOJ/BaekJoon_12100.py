# 2048(Easy)

import sys
input = sys.stdin.readline

N = int(input().rstrip())
board = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]

def row_trial(board_row):
    res, line = [], []
    for e in board_row:
        if e != 0:
            if line and line[-1] == e:
                line.append(line.pop() * 2)
                res.extend(line)
                line = []
            else:
                line.append(e)
    for _ in range(len(line) + len(res), N):
        line.append(0)
    res.extend(line)
    return res

def trial(d, test_board):
    res_board = []
    if d == 'L':
        for r in range(N):
            res_board.append(row_trial(test_board[r]))
    elif d == 'R':
        for r in range(N):
            res_board.append(row_trial(test_board[r][::-1]))
    elif d == 'U':
        for c in range(N):
            res_board.append(row_trial(list(zip(*test_board))[c]))
        res_board = [col for col in list(zip(*res_board))]
    elif d == 'D':
        for c in range(N):
            res_board.append(row_trial(list(zip(*test_board))[c][::-1]))
        res_board = [col for col in list(zip(*res_board))]
    return res_board


def back_tracking(count, board):
    global answer
    if count == 5:
        answer = max(answer, max([max(board[r]) for r in range(N)]))
        return
    else:
        back_tracking(count + 1, trial('L', board[:]))
        back_tracking(count + 1, trial('R', board[:]))
        back_tracking(count + 1, trial('U', board[:]))
        back_tracking(count + 1, trial('D', board[:]))
    return


answer = 0
back_tracking(0, board[:])
print(answer)
