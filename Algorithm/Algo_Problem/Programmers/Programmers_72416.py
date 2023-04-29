def solution(sales, links):
    answer = 0
    INF = int(1e9)

    tree = [[] for _ in range(len(sales) + 1)]
    for link in links:
        tree[link[0]].append(link[1])

    table = [[INF for _ in range(len(sales) + 1)] for _ in range(2)]

    def dfs(curr):
        total = 0
        for t in tree[curr]:
            dfs(t)
            total += min(table[0][t], table[1][t])

        table[1][curr] = sales[curr - 1]
        for t in tree[curr]:
            table[0][curr] = min(table[0][curr], total - min(table[0][t], table[1][t]) + table[1][t])
            table[1][curr] += min(table[0][t], table[1][t])

        if table[0][curr] == INF:
            table[0][curr] = 0

    dfs(1)
    answer = min(table[0][1], table[1][1])
    return answer
