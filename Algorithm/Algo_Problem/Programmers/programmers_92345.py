# 2022 카카오 블라인드 채용
# 사라지는 발판
# https://programmers.co.kr/learn/courses/30/lessons/92345

from collections import deque

def solution(board, aloc, bloc):
    answer = -1
    row, col = len(board), len(board[0])
    before = [-1, -1]
    turn = 0  # A: 0 , B: 1
    res = []

    def is_end_game(r, c, count):
        if not board[r][c]:
            return True

        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= nr < row and 0 <= nc < col and board[nr][nc]:
                return False

        return True

    def process_turn(t, count, aloc, bloc):
        w, M = 0, 100
        curr_r, curr_c = aloc[:] if not t else bloc[:]
        print(t, aloc, bloc, count)
        if is_end_game(curr_r, curr_c, count):
            print('win', t ^ 1, count, aloc, bloc)
            M = min(M, count)
            res.append((count, M))
            return set([t ^ 1]), M
        else:
            winner_set = set()
            # turn A
            if t == 0:
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < row and 0 <= nc < col and board[nr][nc]:
                        before = aloc[:]
                        board[aloc[0]][aloc[1]] = 0
                        aloc = [nr, nc][:]

                        w, x = process_turn(t ^ 1, count + 1, aloc, bloc)
                        winner_set |= w

                        aloc = before[:]
                        board[aloc[0]][aloc[1]] = 1
                        M = min(M, x)
                if len(winner_set) == 1:
                    M = min(M, x)
                    if not M:
                        res.append((count, M))

            # turn B
            if t == 1:
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr, nc = curr_r + dr, curr_c + dc
                    if 0 <= nr < row and 0 <= nc < col and board[nr][nc]:
                        before = bloc[:]
                        board[bloc[0]][bloc[1]] = 0
                        bloc = [nr, nc][:]

                        w, x = process_turn(t ^ 1, count + 1, aloc, bloc)
                        winner_set |= w

                        bloc = before[:]
                        board[bloc[0]][bloc[1]] = 1
                        M = min(M, x)

                if len(winner_set) == 1:
                    M = min(M, x)
                    if not M:
                        res.append((count, M))

        return winner_set, M

    who, answer = process_turn(turn, 0, aloc, bloc)
    print(sorted(res))
    return answer