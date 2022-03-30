# 플로이드-워셜 알고리즘
# 다이나믹 프로그래밍 기반 모든 노드에서 모든 노드 까지의 최단 거리를 구해내는 알고리즘
# a -> b 또는 a -> k -> b 경로 중 비용이 적은 것을 선택
# 점화식: min(D(ab), D(ak) + D(kb))

INF = int(1e9)

# n: 노드의 개수
# m: 간선의 개수
n, m = map(int, input().split(' '))

# 2차원 리스트로 그래프를 표현
graph = [[INF for __ in range(n + 1)] for _ in range(n + 1)]

# a: 출발 노드
# b: 도착 노드
for a in range(n + 1):
    for b in range(n + 1):
        graph[a][b] = 0

# 간선에 대한 비용정보를 입력, 그래프에 저장
for _ in range(m):
    a, b, cost = map(int, input().split(' '))
    graph[a][b] = cost

# 플로이드-워셜 알고리즘 수행
# a -> b 또는 a -> k -> b 중 비용이 적은 것을 그래프에 저장
for k in range(n + 1):
    for a in range(n + 1):
        for b in range(n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for a in range(n + 1):
    for b in range(n + 1):
        if graph[a][b] == INF:
            # can't go == -1
            print(-1)
        else:
            print(graph[a][b])
    print('\n')