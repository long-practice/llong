# 도시 분할 계획

# 해결방법
# 남은 유지비의 합의 최솟값은 최소 신장트리를 구하고
# 간선 비용이 가장 큰 간선을 추가로 제거하여 최종 유지비 계산

# 입력 예시
# 7 12
# 1 2 3
# 1 3 2
# 3 2 1
# 2 5 2
# 3 4 4
# 7 3 6
# 5 1 5
# 1 6 2
# 6 4 1
# 6 5 3
# 4 5 3
# 6 7 4

# 출력 예시
# 8

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    A, B = find(a), find(b)

    if A < B:
        parent[B] = A
    else:
        parent[A] = B

# 노드 개수, 간선 개수 입력, 부모 테이블 초기화
v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

# 간선에 대한 정보 입력
edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))
edges.sort()

# 최소 신장트리 구성(Kruskal 알고리즘)
answer = 0
# last는 최소 신장 트리에서 가장 비용이 큰 간선
last = 0
for edge in edges:
    cost, a, b = edge
    if find(a) != find(b):
        union(a, b)
        answer += cost
        last = cost

print(answer - last)