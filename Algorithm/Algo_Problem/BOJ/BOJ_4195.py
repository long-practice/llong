import sys
sys.setrecursionlimit(int(1e5))
input = sys.stdin.readline


def find(x):
    if x != parent[x]:
        parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    A, B = find(a), find(b)
    if A != B:
        A, B = max(A, B), min(A, B)
        fri_net_count[B] += fri_net_count[A]
    parent[A] = B
    return fri_net_count[B]


for _ in range(int(input().rstrip())):
    fri_net_count = {}
    parent = {}
    for _ in range(int(input().rstrip())):
        a, b = input().rstrip().split()
        if a not in fri_net_count:
            parent[a] = a
            fri_net_count[a] = 1

        if b not in fri_net_count:
            parent[b] = b
            fri_net_count[b] = 1

        print(union(a, b))
