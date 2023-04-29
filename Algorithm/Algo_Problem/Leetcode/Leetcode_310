import heapq


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)


        def dijkstra(start):
            dist = [int(1e9) for _ in range(n)]

            h, dist[start] = [(0, start)], 0
            while h:
                cost, curr = heapq.heappop(h)
                if dist[curr] <= cost:
                    for g in graph[curr]:
                        if cost + 1 <= dist[g]:
                            dist[g] = cost + 1
                            heapq.heappush(h, (cost + 1, g))

            dist = [x if x != int(1e9) else -1 for x in dist]
            return dist


        def get_longest_path(node):
            path.append(node)
            if len(path) == diameter + 1:
                return True

            for g in graph[node]:
                if get_longest_path(g):
                    return True
            path.pop()
            return False


        dist_from_random_node = dijkstra(0)
        farest = dist_from_random_node.index(max(dist_from_random_node))
        get_diameter = dijkstra(farest)
        diameter = max(get_diameter)
        path = []
        get_longest_path(farest)

        idx = []
        if len(path) % 2:
            idx.extend([len(path) // 2])
        else:
            idx.extend([len(path) // 2 - 1, len(path) // 2])

        return [path[i] for i in idx]