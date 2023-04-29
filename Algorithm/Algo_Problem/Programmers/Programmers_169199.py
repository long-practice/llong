from collections import deque

def solution(board):
    answer = -1

    R, C = len(board), len(board[0])
    visited = [[False for _ in range(C)] for _ in range(R)]
    start = end = None
    for row in range(R):
        for col in range(C):
            if board[row][col] == 'R':
                start = (row, col)
            if board[row][col] == 'G':
                end = (row, col)


    def findNextPos(currRow, currCol, dr, dc):
        nextRow, nextCol = currRow, currCol

        while isInBoard(nextRow + dr, nextCol + dc) and board[nextRow + dr][nextCol + dc] != 'D':
            nextRow += dr
            nextCol += dc

        return True, nextRow, nextCol


    def isInBoard(row, col):
        return 0 <= row < R and 0 <= col < C


    q = deque([(start[0], start[1], 0)])
    visited[start[0]][start[1]] = True
    while q:
        currRow, currCol, count = q.popleft()
        if currRow == end[0] and currCol == end[1]:
            answer = count
            break

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            canMove, nextRow, nextCol = findNextPos(currRow, currCol, dr, dc)
            if canMove and not visited[nextRow][nextCol]:
                visited[nextRow][nextCol] = True
                q.append((nextRow, nextCol, count + 1))

    return answer