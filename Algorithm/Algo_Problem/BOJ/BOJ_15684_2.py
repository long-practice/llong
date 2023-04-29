import sys
input = sys.stdin.readline

N, M, H = map(int, input().rstrip().split())
ladders = [tuple(map(int, input().rstrip().split())) for _ in range(M)]

board = [[False for _ in range(N + 1)] for _ in range(H + 1)]
col_ladder_count = [0 for _ in range(N)]
for ladder in ladders:
    r, c = ladder
    board[r][c] = True
    col_ladder_count[c] += 1


# 사다리 구현 확인
# from pprint import pprint
# pprint(board)


# 사다리는 최대 3개
answer = 4


# 사다리 게임 결과 확인 함수
def well_set():
    for c in range(1, N):
        col_res = c
        for r in range(1, H + 1):
            if board[r][col_res]:
                col_res += 1
            elif board[r][col_res - 1]:
                col_res -= 1
        if col_res != c:
            return False
    return True


# 이터레이터 스킵 함수
def skip_iter(iterator, n):
    for _ in range(n):
        try:
            next(iterator)
        except StopIteration:
            break
    return


# 사다리를 하나씩 놓아보는 함수
def set_ladder(ladder_count, curr_r, curr_c):
    global answer
    if ladder_count >= answer:
        return

    if well_set():
        answer = min(answer, ladder_count)
        return

    # 반드시 각 세로 구간에는 사다리가 짝수개가 위치해야 i -> i 도달 가능
    odd_ladder = sum(x & 1 for x in col_ladder_count)
    if odd_ladder <= 3 - ladder_count:
        for row in range(curr_r, H + 1):
            if row != curr_r:
                curr_c = 1

            # 한 번에 col을 2개 혹은 3개 스킵하기 위해서 이터레이터 구현
            col_iterator = iter(range(curr_c, N))
            for col in col_iterator:
                if board[row][col + 1]:
                    skip_iter(col_iterator, 2)
                elif board[row][col]:
                    skip_iter(col_iterator, 1)
                else:
                    board[row][col] = True
                    col_ladder_count[col] += 1

                    set_ladder(ladder_count + 1, row, col + 2)

                    col_ladder_count[col] -= 1
                    board[row][col] = False
    return


set_ladder(0, 1, 1)
print(answer if answer < 4 else -1)