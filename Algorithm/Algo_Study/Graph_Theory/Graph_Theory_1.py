# 팀 결성

# 해결 방법
# 팀 합치기 연산 == union 함수로 구현
# 같은 팀 여부 확인 == find 함수로 확인
# 백준 1717번(집합의 표현)과 동일한 문제

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

N, M = map(int, input().rstrip().split(' '))
parent = [i for i in range(N + 1)]

for _ in range(M):
    command, a, b = map(int, input().rstrip().split(' '))
    if command == 0:
        union(a, b)
    else:
        print("NO") if find(a) != find(b) else print("YES")