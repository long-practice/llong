def solution(arr):
    answer = [0, 0]

    def checkPress(rangeRow, rangeCol, num):
        for row in rangeRow:
            for col in rangeCol:
                if arr[row][col] != num:
                    return False
        return True

    def search(minRow, maxRow, minCol, maxCol):
        num = arr[minRow][minCol]
        canPress = checkPress(range(minRow, maxRow), range(minCol, maxCol), num)

        if canPress:
            answer[num] += 1
        else:
            midRow, midCol = (minRow + maxRow) // 2, (minCol + maxCol) // 2
            search(minRow, midRow, minCol, midCol)
            search(minRow, midRow, midCol, maxCol)
            search(midRow, maxRow, minCol, midCol)
            search(midRow, maxRow, midCol, maxCol)

    search(0, len(arr), 0, len(arr))

    return answer