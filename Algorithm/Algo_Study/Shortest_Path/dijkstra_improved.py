# 개선된 다익스트라 알고리즘
# 우선순위 큐(priority queue) 이용
# 최단 거리가 가장 짧은 노드를 선형적으로 탐색하는 것이 아닌 더욱더 빠르게 찾는 방법 이용

# 입력 예시
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

# 출력 예시
# 0
# 2
# 3
# 1
# 2
# 4

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]
distance = [INF for _ in range(n + 1)]

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))

def dijkstra(start):
    queue = []

    # (cost, node)
    heapq.heappush(queue, (0, start))
    distance[start] = 0

    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        # i에는 now와 인접한 노드와 그 비용 정보가 들어있음. (인접 노드, 비용)
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(queue, (cost, i[0]))

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:
        print("can't go")
    else:
        print("To go ", i, ", You need cost ", distance[i])