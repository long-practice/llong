def solution(key, lock):
    M, N = len(key), len(lock)
    board = [[1 for _ in range(N + 2 * (M - 1))] for _ in range(N + 2 * (M - 1))]

    for r in range(N):
        for c in range(N):
            board[(M - 1) + r][(M - 1) + c] = lock[r][c]

    def UseKey(row, col, currKey):
        for dr in range(M):
            for dc in range(M):
                board[row + dr][col + dc] ^= currKey[dr][dc]
        return

    def match():
        res = 0
        for dr in range(N):
            for dc in range(N):
                res += board[(M - 1) + dr][(M - 1) + dc]
        return res == N * N

    def rotate(prevKey):
        nextKey = [[0 for _ in range(M)] for _ in range(M)]
        for r in range(M):
            for c in range(M):
                nextKey[r][c] = prevKey[c][(M - 1) - r]
        return nextKey

    for _ in range(4):
        for row in range(M + N - 1):
            for col in range(M + N - 1):
                UseKey(row, col, key)
                if match():
                    return True
                UseKey(row, col, key)
        key = rotate(key)

    return False