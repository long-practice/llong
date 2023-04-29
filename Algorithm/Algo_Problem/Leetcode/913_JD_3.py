from collections import deque
class Solution:
    def catMouseGame(self, graph) -> int:
        n = len(graph)

        degree = [[[0 for k in range(3)] for j in range(n)] for i in range(n)]
        for i in range(n):
            for j in range(n):
                degree[i][j][1] += len(graph[i])
                degree[i][j][2] += len(graph[j])
                if 0 in graph[j]:
                    degree[i][j][2] -= 1

        dq = deque()
        win = [[[0 for k in range(3)] for j in range(n)] for i in range(n)]
        for i in range(1, n):
            for k in range(1, 3):
                win[0][i][k] = 1
                dq.append([0, i, k, 1])
                win[i][i][k] = 2
                dq.append([i, i, k, 2])

        while dq:
            m, c, t, w = dq.popleft()
            print(m, c, t, w)
            parents = []
            if t == 1:
                for parent in graph[c]:
                    if parent != 0:
                        parents.append([m, parent, 2])
            else:
                for parent in graph[m]:
                    parents.append([parent, c, 1])
            for mp, cp, tp in parents:
                if win[mp][cp][tp] == 0:
                    if tp == w:
                        win[mp][cp][tp] = w
                        dq.append([mp, cp, tp, w])
                    else:
                        degree[mp][cp][tp] -= 1
                        if degree[mp][cp][tp] == 0:
                            win[mp][cp][tp] = w
                            dq.append([mp, cp, tp, w])

        return win[1][2][1]