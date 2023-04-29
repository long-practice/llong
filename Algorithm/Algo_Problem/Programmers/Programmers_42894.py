def solution(board):
    answer = 0

    # R: 행의 개수, C: 열의 개수
    R, C = len(board), len(board[0])
    visited = [[False for _ in range(C)] for _ in range(R)]


    # block_point_dict를 만들기 위한 함수
    # board를 탐색하면서 0이 아닌수를 만나면 키는 블록번호, 값은 블록위치를 리스트에 담아서 딕셔너리 구성
    def makeBlockPointDict():
        num_blockpoint_dict = {}
        for row in range(R):
            for col in range(C):
                block_num = board[row][col]
                if not visited[row][col] and block_num:
                    position = (row, col)
                    num_blockpoint_dict[block_num] = num_blockpoint_dict.get(block_num, []) + [position]

        return num_blockpoint_dict


    # need_point_dict를 구성하기 위한 함수
    # 1. 각 블록에 대해서 꽉찼을 때(직사각형을 만족할 때) 상태 구하기
    # 2. 1에서 구한 꽉찼을 때의 point에서 블록이 차지하고 있는 point를 빼기
    #    = 꽉 채우기 위해 차지해야하는 point
    # 3. 각 블록번호를 키, 2에서 구한 리스트를 값으로 딕셔너리 구성
    def makeNeedPointToBeFullDict():
        need_point_dict = {}

        for block_num, block_points in block_point_dict.items():
            rectengular = makeFullRectengularBlock(block_points)
            need_points = set(rectengular) - set(block_points)
            need_point_dict[block_num] = list(need_points)

        return need_point_dict


    # 각 블록에 대해서 row 혹은 col의 최대, 최소값을 이용하여 range 구성
    # 구성한 range에 대해 직사각형 범위의 좌표를 구하기
    def makeFullRectengularBlock(block_points):
        rangeRow, rangeCol = getBlockRange(block_points)
        rectengular_points = [(row, col) for col in rangeCol for row in rangeRow]
        return rectengular_points


    # 각 블록을 꽉채웠을 때 가장 자리 4개 좌표, 즉, row, col의 최대 최소값 구하기
    def getBlockRange(points):
        minRow, maxRow = 50, 0
        minCol, maxCol = 50, 0

        for point in points:
            point_row, point_col = point
            minRow, maxRow = min(minRow, point_row), max(maxRow, point_row)
            minCol, maxCol = min(minCol, point_col), max(maxCol, point_col)

        rangeRow, rangeCol = range(minRow, maxRow + 1), range(minCol, maxCol + 1)
        return rangeRow, rangeCol


    # 검은 블록을 두 개씩 떨어뜨릴 때 어느 위치에 떨어지는지 구하는 함수
    def drop_black_block():
        drop_points = []
        for board_col in range(C):
            for board_row in range(R):
                if board[board_row][board_col]:
                    if board_row - 1 >= 0:
                        drop_points.append((board_row - 1, board_col))
                    if board_row - 2 >= 0:
                        drop_points.append((board_row - 2, board_col))
                    break
            else:
                drop_points.append((R - 1, board_col))
                drop_points.append((R - 2, board_col))
        return drop_points


    # 블록을 지울 때 board를 업데이트하는 함수
    def removeBlockInBoard(points):
        for point in points:
            row, col = point
            board[row][col] = 0


    # block_point_dict: 각 블록번호에 대한 블록위치 ex) 1: [(0, 0), (0, 1), (0, 2), (1, 0)]
    # need_block_dict: 각 블록번호에 대해 채워야하는 블록위치 ex) 1: [(1, 1), (1, 2)]
    block_point_dict = makeBlockPointDict()
    need_block_dict = makeNeedPointToBeFullDict()


    # 블록이 없어지지 않을 때까지 반복
    # 1. 검은 블록을 2개씩 떨어뜨리기
    # 2. 각 블록에 대해서 없애기 위해 채워져야하는 곳에 검은 블록이 떨어지는지 확인
    # 3. 블록을 없앨 수 있으면(검은 블록이 채워져야하는 곳에 떨어지면) 블록 제거, board업데이트
    # 4. answer 업데이트
    remove_block = 1
    while remove_block:
        remove_block = 0
        drop_points = drop_black_block()
        for block_num in need_block_dict.keys():
            need_blocks = set(need_block_dict[block_num])
            if not need_blocks:
                continue
            intersact_NeedBlock_DropPoints = set(need_block_dict[block_num]) & set(drop_points)
            possibleRemove = intersact_NeedBlock_DropPoints == need_blocks
            if possibleRemove:
                remove_block += 1
                removeBlockInBoard(block_point_dict[block_num])
                need_block_dict[block_num].clear()
        answer += remove_block

    return answer
