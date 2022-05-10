# 2020 카카오 인턴십
# [카카오 인턴] 동굴탐험
# https://programmers.co.kr/learn/courses/30/lessons/67260

import sys
sys.setrecursionlimit(int(2e5) + 10)
from collections import deque

def solution(n, path, order):
    pre = {i: 0 for i in range(n)}
    visited = [False for _ in range(n)]
    visited[0] = True

    graph = [[] for _ in range(n)]
    for p in path:
        graph[p[0]].append(p[1])
        graph[p[1]].append(p[0])

    for o in order:
        pre[o[1]] = o[0]

    q = deque([0])
    cannot_visit = 0


    def dfs(curr):
        visited[curr] = True
        for g in graph[curr]:
            if not visited[g]:
                if visited[pre[g]]:
                    dfs(g)
                else:
                    q.append(g)
        return


    while q:
        curr = q[0]

        if visited[pre[curr]]:
            q.popleft()
            cannot_visit = 0
            dfs(curr)
        else:
            q.rotate(-1)
            cannot_visit += 1
            if cannot_visit == len(q):
                return False

    return True