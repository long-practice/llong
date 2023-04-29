from collections import deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n - 1:
            graph = [[] for _ in range(n)]
            degrees = [0 for _ in range(n)]
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)
                degrees[a] += 1
                degrees[b] += 1

            rest = n
            q = deque([])
            for i in range(n):
                if degrees[i] == 1:
                    degrees[i] -= 1
                    q.append(i)

            while rest > 2:
                rest -= len(q)
                for _ in range(len(q)):
                    node = q.popleft()
                    for g in graph[node]:
                        if degrees[g]:
                            degrees[g] -= 1
                            if degrees[g] == 1:
                                q.append(g)
            return q
        else:
            return [0]