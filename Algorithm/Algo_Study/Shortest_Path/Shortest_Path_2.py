# 전보

# 풀이방법
# C노드 기준으로 다익스트라 적용
# 각 노드까지의 거리중 최대 거리인 것을 선택
# 이 때 거리가 INF인 것은 이동할 수 없는 노드이므로 제외

import heapq
import sys
def input():
    return sys.stdin.readline().rstrip()

# N: 도시 개수, M: 통로 개수, C: 메시지를 보내고자 하는 도시
N, M, C = map(int, input().split(' '))

graph = [[] for _ in range(N + 1)]
INF = int(1e9)

for _ in range(M):
    a, b, cost = map(int, input().split(' '))
    graph[a].append((cost, b))
dist = [INF for _ in range(N + 1)]

def dijkstra(C):
    # 최초 시작하는 도시: C
    # 이 때 이동거리(소요): 0
    Q = []
    heapq.heappush(Q, (0, C))
    dist[C] = 0

    while Q:
        d, curr = heapq.heappop(Q)

        if dist[curr] < d:
            continue

        for g in graph[curr]:
            cost = d + g[0]
            if dist[g[1]] > cost:
                dist[g[1]] = cost
                heapq.heappush(Q, (cost, g[1]))
dijkstra(C)

# 도달할 수 있는 도시의 수
count = 0
max_dist = 0
for i in range(1, N + 1):
    if dist[i] != INF:
        count += 1
        max_dist = max(max_dist, dist[i])

# 본인 노드는 제외해야 하므로 count - 1
print(count - 1, max_dist)