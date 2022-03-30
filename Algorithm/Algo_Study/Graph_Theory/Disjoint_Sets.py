# 서로소 집합

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
parent = [0 for _ in range(v + 1)]

# 부모 테이블 초기화
for i in range(1, v + 1):
    parent[i] = i

# union 연산 수행
for i in range(e):
    a, b = map(int, input().split(' '))
    union(parent, a, b)

print('각 원소가 속한 집합 출력: ', end=' ')
for i in range(1, v + 1):
    print(find(parent, i), end=' ')
print()

print('부모 테이블: ', end=' ')
for i in range(1, v + 1):
    print(parent[i], end=' ')

