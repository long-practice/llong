import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[] for _ in range(n + 1)]
        cost = [int(1e9) for _ in range(n + 1)]
        cost[0] = 0

        for time in times:
            graph[time[0]].append((time[2], time[1]))

        def dijkstra(start):
            h = [(0, start)]
            cost[start] = 0
            while h:
                c, curr = heapq.heappop(h)

                if cost[curr] <= c:
                    for g in graph[curr]:
                        if c + g[0] < cost[g[1]]:
                            cost[g[1]] = c + g[0]
                            heapq.heappush(h, (c + g[0], g[1]))

        dijkstra(k)
        ans = max(cost)
        return max(cost) if ans != 1e9 else -1