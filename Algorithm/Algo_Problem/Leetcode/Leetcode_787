from collections import deque

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        cost = [int(1e9) for _ in range(n)]

        for flight in flights:
            graph[flight[0]].append((flight[2], flight[1]))

        q = deque([(0, src, -1)])
        cost[src] = 0
        while q:
            c, curr, k_count = q.popleft()

            for g in graph[curr]:
                if k_count < k and c + g[0] < cost[g[1]]:
                    cost[g[1]] = c + g[0]
                    q.append((c + g[0], g[1], k_count + 1))

        return -1 if cost[dst] == int(1e9) else cost[dst]
