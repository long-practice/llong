def floyd_warshall(n, graph):
    for i in range(n + 1):
        graph[i][i] = 0

    for k in range(1, n + 1):
        for a1 in range(1, n + 1):
            for a2 in range(1, n + 1):
                if a1 != a2:
                    graph[a1][a2] = min(graph[a1][a2], graph[a1][k] + graph[k][a2])

    return graph


def solution(n, s, a, b, fares):
    INF = int(1e9)
    graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
    answer = INF

    for fare in fares:
        x, y, c = fare
        graph[x][y] = graph[y][x] = c
    graph = floyd_warshall(n, graph)

    for k in range(1, n + 1):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])

    return answer

