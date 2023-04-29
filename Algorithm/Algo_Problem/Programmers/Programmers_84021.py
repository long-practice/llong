def solution(game_board, table):
    def make_piece(board, row, col, v):
        piece = dfs(board, row, col, [], v)
        return make_fully(*preprocess(piece))

    def dfs(board, r, c, tr, v):
        board[r][c] = v ^ 1
        tr.append((r, c))
        for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
            if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == v:
                tr = dfs(board, nr, nc, tr, v)
        return tr

    def preprocess(point_ls):
        zip_ls = list(zip(*point_ls))
        mr, mc = min(zip_ls[0]), min(zip_ls[1])
        Mr, Mc = max(zip_ls[0]), max(zip_ls[1])
        return [(r - mr, c - mc) for r, c in point_ls], range(mr, Mr + 1), range(mc, Mc + 1)

    def make_fully(tr, rangeRow, rangeCol):
        each_block = [[0 for _ in rangeCol] for _ in rangeRow]
        for r, c in tr:
            each_block[r][c] = 1
        return each_block

    def extract(board, v):
        piece_dict, i = {}, 0
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == v:
                    i += 1
                    piece_dict[i] = piece_dict.get(i, [])
                    piece = make_piece(board, row, col, v)
                    piece_dict[i].append(piece)
                    if v:
                        for _ in range(3):
                            piece = rotate_piece(piece)
                            piece_dict[i].append(piece)
                    else:
                        block_count[i] = sum(sum(p_row) for p_row in piece)
        return piece_dict

    def rotate_piece(piece):
        pr, pc = len(piece), len(piece[0])
        new_piece = [[0 for _ in range(pr)] for _ in range(pc)]
        for r in range(pr):
            for c in range(pc):
                new_piece[c][pr - 1 - r] = piece[r][c]
        return new_piece

    answer = 0
    block_count = {}
    blank_dict = extract(game_board, 0)
    block_dict = extract(table, 1)

    block_used = [False for _ in range(max(block_dict.keys()) + 1)]
    for blankNum, blank in blank_dict.items():
        for blockNum, block in block_dict.items():
            if not block_used[blockNum] and blank[0] in block:
                block_used[blockNum] = True
                answer += block_count[blankNum]
                break

    return answer