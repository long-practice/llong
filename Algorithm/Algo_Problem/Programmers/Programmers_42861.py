def solution(n, costs):
    answer = 0

    def find(parent, x):
        if parent[x] != x:
            parent[x] = find(parent, parent[x])
        return parent[x]

    def union(parent, a, b):
        a, b = find(parent, a), find(parent, b)
        parent[max(a, b)] = min(a, b)

    graph = [[] for _ in range(n)]
    parent = [i for i in range(n)]
    V = []

    for cost in costs:
        a, b, c = cost
        graph[a] = b
        V.append((c, a, b))

    V.sort()
    for v in V:
        c, a, b = v
        if find(parent, a) != find(parent, b):
            answer += c
            union(parent, a, b)

    return answer