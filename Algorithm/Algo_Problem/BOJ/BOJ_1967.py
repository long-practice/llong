import heapq

import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4) * 3)

N = int(input().rstrip())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, l = map(int, input().rstrip().split())
    tree[a].append((b, l))
    tree[b].append((a, l))


def dijkstra(start):
    distance = [int(1e9) for _ in range(N + 1)]
    distance[start] = 0

    h = [(0, start)]
    while h:
        cost, curr = heapq.heappop(h)

        if cost <= distance[curr]:
            for node, c in tree[curr]:
                if cost + c < distance[node]:
                    distance[node] = cost + c
                    heapq.heappush(h, (cost + c, node))

    for i in range(len(distance)):
        if distance[i] == int(1e9):
            distance[i] = -1

    return distance

first_dijk = dijkstra(1)
far_node = first_dijk.index(max(first_dijk))
second_dijk = dijkstra(far_node)
print(max(second_dijk))