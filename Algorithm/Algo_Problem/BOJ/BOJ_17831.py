import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(2e5)+10)

N = int(input().rstrip())
tree = [[] for _ in range(N + 1)]

link = list(map(int, input().rstrip().split()))
score = list(map(int, input().rstrip().split()))
for i in range(len(link)):
    tree[link[i]].append(i + 2)

for node in range(1, N + 1):
    print(f'node:{node}, score:{score[node - 1]}, children:{tree[node]}')

table = [[0 for _ in range(N + 1)] for _ in range(2)]

def dfs(curr):
    for t in tree[curr]:
        dfs(t)
        table[0][curr] += max(table[1][t], table[0][t])

    for t in tree[curr]:
        mentoring_score = score[curr - 1] * score[t - 1] + table[0][t]
        table[1][curr] = max(table[1][curr], table[0][curr] - max(table[0][t], table[1][t]) + mentoring_score)

dfs(1)
print(max(table[0][1], table[1][1]))

