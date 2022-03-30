# 최소 공통 조상
# 두 노드의 공통된 조상 중 가장 가까운 조상을 찾는 문제

# 1. 모든 노드에 대한 깊이(depth)를 계산
# 2. 최소 공통 조상을 찾을 두 노드 확인
#    두 노드의 깊이가 동일하도록 거슬러 올라감
#    이후 부모가 같아질 때 까지 반복적으로 두 노드의 부모 방향으로 거슬러 올라감
# 3. 2.반복

import sys
sys.setrecursionlimit(int(1e5))
n = int(input())

parent = [0 for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]
is_checked = [False for _ in range(n + 1)]
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().rstrip().split(' '))
    graph[a].append(b)
    graph[b].append(a)


# 깊이(depth)를 구하는 함수
def dfs(x, d):
    is_checked[x] = True
    depth[x] = d
    for g in graph[x]:
        if is_checked[g]:
            continue
        parent[g] = x
        dfs(g, d + 1)

# A, B의 최소 공통 조상을 찾는 함수
# 1. 깊이를 동일하게 맞춰준 다음
# 2. 하나씩 부모 노드로 이동하면서 동일한 노드를 가리킬 시 함수 종료
def lca(a, b):
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]

    while a != b:
        a = parent[a]
        b = parent[b]
    return a

# 루트 노드(1번)에 대해 깊이를 구해주기
dfs(1, 0)

m = int(input())

for i in range(m):
    a, b = map(int, input().split())
    print(lca(a, b))