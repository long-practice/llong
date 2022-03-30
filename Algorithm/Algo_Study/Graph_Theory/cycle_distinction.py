# 사이클 판별

# 서로소 집합을 이용
# union을 통해 간선을 구성한다고 생각하면 됨
# 매 반복마다 union 수행하기 전에 제일 꼭대기에 있는 parent가 서로 같으면 cycle발생
def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    A = find(parent, a)
    B = find(parent, b)

    if A < B:
        parent[B] = A
    else: # A > B
        parent[A] = B

# v: 노드 개수, e: 간선(union 연산) 개수
v, e = map(int, input().split(' '))
# 부모 테이블 초기화
parent = [i for i in range(v + 1)]

cycle = False

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split(' '))
    if find(parent, a) == find(parent, b):
        cycle = True
        break
    else:
        union(parent, a, b)

if cycle:
    print("사이클이 발생했습니다.")
else:
    print("사이클이 발생하지 않았습니다.")