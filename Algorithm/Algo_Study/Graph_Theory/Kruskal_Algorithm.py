# 크루스칼 알고리즘

# 그리디 알고리즘 이용
# 최소 신장 트리를 구성하기 위해 우선 비용을 오름차순으로 정렬한 후
# 가장 낮은 비용의 경로를 선택
# 만약 가장 낮은 비용의 경로를 선택해서 두 지점을 연결했을 때 사이클이 발생한다면 연결하지 않고 다음 경로 선택

# 입력 예시
# 7 9
# 1 2 29
# 1 5 75
# 2 3 35
# 2 6 34
# 3 4 7
# 4 6 23
# 4 7 13
# 5 6 53
# 6 7 25

# 출력 예시
# 159

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    A = find(parent, a)
    B = find(parent, b)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B


v, e = map(int, input().rstrip().split(' '))

# 간선을 담을 리스트, 부모테이블 초기화
edges = []
result = 0
parent = [i for i in range(v + 1)]

# 간선 정보 입력
for _ in range(e):
    a, b, cost = map(int, input().rstrip().split(' '))
    # 비용을 오름차순으로 정렬하기 위해 cost를 먼저 배치
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    # 사이클 여부 확인
    if find(parent, a) != find(parent, b):
        union(parent, a, b)
        result += cost

print(result)