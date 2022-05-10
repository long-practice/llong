# 2020 카카오 인턴십
# [카카오 인턴] 동굴탐험
# https://programmers.co.kr/learn/courses/30/lessons/67260

import sys
sys.setrecursionlimit(int(2e5) + 10)
from collections import deque


def solution(n, path, order):
    visited = [False for _ in range(n)]
    graph = [[] for _ in range(n)]

    for p in path:
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])

    direct_graph = [[] for _ in range(n)]

    q = deque([0])
    visited[0] = True
    while q:
        node = q.pop()
        for g in graph[node]:
            if not visited[g]:
                visited[g] = True
                q.append(g)
                direct_graph[node].append(g)

    for o in order:
        direct_graph[o[0]].append(o[1])

    visited = [False for _ in range(n)]
    visited2 = [False for _ in range(n)]


    def dfs(node):
        visited[node] = True

        for dg in direct_graph[node]:
            if not visited2[dg]:
                if visited[dg]:
                    return False
                if not dfs(dg):
                    return False

        visited2[node] = True
        return True

    return dfs(0)