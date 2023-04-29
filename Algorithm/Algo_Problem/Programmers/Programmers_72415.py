from collections import deque


def solution(board, r, c):
    answer = 0
    visited = set()

    def appendQueue(bboard, row, col, count, card):
        if (bboard, row, col, card) not in visited:
            visited.add((bboard, row, col, card))
            q.append((bboard, row, col, count, card))


    bit_board = 0
    for idx in range(16):
        if board[idx // 4][idx % 4]:
            bit_board |= 1 << idx

    q = deque([(bit_board, r, c, 0, 0)])
    visited.add((bit_board, r, c, 0))
    while q:
        curr_board, cr, cc, count, curr_card = q.popleft()
        if not curr_board:
            answer = count
            break

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = cr + dr, cc + dc
            if 0 <= nr < 4 and 0 <= nc < 4:
                appendQueue(curr_board, nr, nc, count + 1, curr_card)
                while 0 <= nr + dr < 4 and 0 <= nc + dc < 4 and not curr_board & 1 << 4 * nr + nc:
                    nr, nc = nr + dr, nc + dc
                appendQueue(curr_board, nr, nc, count + 1, curr_card)

        board_idx = 4 * cr + cc
        if curr_card:
            if curr_board & (1 << board_idx) and board[cr][cc] == curr_card:
                curr_board &= ~(1 << board_idx)
                appendQueue(curr_board, cr, cc, count + 1, 0)
        else:
            if curr_board & (1 << board_idx) and board[cr][cc]:
                curr_board &= ~(1 << board_idx)
                appendQueue(curr_board, cr, cc, count + 1, board[cr][cc])

    return answer