from collections import deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        all_chr = set()
        for e in equations:
            all_chr |= set(e)

        chr_idx = {c: i for i, c in enumerate(all_chr)}
        graph = [[] for _ in range(len(chr_idx.keys()))]

        for e, v in zip(equations, values):
            e[0], e[1] = chr_idx[e[0]], chr_idx[e[1]]
            graph[e[0]].append((e[1], v))
            graph[e[1]].append((e[0], 1/v))

        def get_ans(start, end):
            answer = -1.0
            visited = [False for _ in range(26)]

            q = deque()
            q.append((start, 1.0))
            while q:
                node, val = q.popleft()
                if node == end:
                    answer = val
                    break

                for g in graph[node]:
                    next_node, weight = g[0], g[1]
                    if not visited[next_node]:
                        visited[next_node] = True
                        q.append((next_node, val * weight))
            return answer

        answer = []
        for query in queries:
            if query[0] in chr_idx.keys() and query[1] in chr_idx.keys():
                answer.append(get_ans(chr_idx[query[0]], chr_idx[query[1]]))
            else:
                answer.append(-1)
        return answer