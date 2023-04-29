def solution(n, m, x, y, queries):
    answer = 0
    rcQuery = [[] for _ in range(2)]
    for query in queries:
        sign = (query[0] % 2) * 2 - 1
        rcQuery[query[0] // 2].append(sign * query[1])

    def func(rclist, low, high, loc):
        lowPoints, highPoints = 1, 1
        allPoints = high - low + 1

        for value in rclist:
            low += value
            high += value

            if low < 0:
                overPoints = -low + (lowPoints - 1)
                lowPoints = 1 + overPoints
                low = 0
                high = max(0, high)

            if high > allPoints - 1:
                overPoints = high - (allPoints - 1) + (highPoints - 1)
                highPoints = 1 + overPoints
                high = allPoints - 1
                low = min(allPoints - 1, low)

        if low == high:
            lowPoints = highPoints = allPoints

        if low == loc:
            return lowPoints
        elif low < loc < high:
            return 1
        elif high == loc:
            return highPoints
        else:
            return 0

    col, row = func(rcQuery[0], 0, m - 1, y), func(rcQuery[1], 0, n - 1, x)
    answer = col * row

    return answer