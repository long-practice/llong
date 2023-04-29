def solution(n, build_frame):
    answer = []

    construct_frame = [[[0 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(2)]
    typeBar, typeCover = 0, 1

    def CanBuildBar(row, col):
        if col == 0:
            return True

        LeftCover = row - 1 >= 0 and construct_frame[typeCover][row - 1][col]
        RightCover = row + 1 <= n and construct_frame[typeCover][row + 1][col]
        if LeftCover or RightCover:
            return True

        UnderBar = col - 1 >= 0 and construct_frame[typeBar][row][col - 1]
        if UnderBar:
            return True

        return False

    def CanBuildCover(row, col):
        LeftBar = col - 1 >= 0 and construct_frame[typeBar][row][col - 1]
        RightBar = col - 1 >= 0 and row + 1 <= n and construct_frame[typeBar][row + 1][col - 1]
        if LeftBar or RightBar:
            return True

        LeftCover = row - 1 >= 0 and construct_frame[typeCover][row - 1][col]
        RightCover = row + 1 <= n and construct_frame[typeCover][row + 1][col]
        if LeftCover and RightCover:
            return True

        return False

    def CanDelete(row, col, typeX):
        construct_frame[typeX][row][col] = 0
        for c in range(col, min(col + 2, n + 1)):
            for r in range(max(row - 1, 0), min(row + 2, n + 1)):
                if construct_frame[typeBar][r][c] and not CanBuildBar(r, c):
                    return False
                if construct_frame[typeCover][r][c] and not CanBuildCover(r, c):
                    return False
        return True

    for query in build_frame:
        r, c, cover, build = query
        bar, remove = cover ^ 1, build ^ 1

        if bar and build:
            if CanBuildBar(r, c):
                construct_frame[typeBar][r][c] = 1

        elif bar and remove:
            if not CanDelete(r, c, typeBar):
                construct_frame[typeBar][r][c] = 1

        elif cover and build:
            if CanBuildCover(r, c):
                construct_frame[typeCover][r][c] = 1

        elif cover and remove:
            if not CanDelete(r, c, typeCover):
                construct_frame[typeCover][r][c] = 1

        else:
            print(f'{query} wrong query')
            print()

    for row in range(n + 1):
        for col in range(n + 1):
            for bar_cover in range(2):
                if construct_frame[bar_cover][row][col]:
                    answer.append([row, col, bar_cover])

    return answer