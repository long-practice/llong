import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4) * 3)

N = int(input().rstrip())
tree = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b, l = map(int, input().rstrip().split())
    tree[a].append((b, l))

answer = [0]
def diameter(node):
    array = [0]
    for n, cost in tree[node]:
        array.append(cost + diameter(n))

    if len(array) > 1:
        array.sort()
        answer.append(array[-1] + array[-2])
    return array[-1]


diameter(1)
print(max(answer))