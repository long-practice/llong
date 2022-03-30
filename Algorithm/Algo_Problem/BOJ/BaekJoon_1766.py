# 문제집

# 문제 조건에 따르면
# 1. 모든 문제를 풀어야함
# 2. 먼저 풀어야하는 문제가 존재(선수 관계를 파악)
# 3. 쉬운 문제부터 풀어야함.

# 문제의 수가 32000개이기 때문에 단순히 O(n**2)로 접근하면 시간 초과가 나므로
# 힙(우선순위 큐)를 이용하여 매 순간 쉬운 문제부터 풀게 하고 위상정렬하여 힙에 진입차수가 0인 문제를 push
import heapq
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4))

N, M = map(int, input().rstrip().split(' '))
graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]
solved = [False for _ in range(N + 1)]
q = []

for _ in range(M):
    a, b = map(int, input().rstrip().split(' '))
    graph[a].append(b)
    indegree[b] += 1

for i in range(1, N + 1):
    if indegree[i] == 0:
        heapq.heappush(q, i)

answer = []
while q:
    curr = heapq.heappop(q)
    answer.append(curr)

    for c in graph[curr]:
        indegree[c] -= 1
        if indegree[c] == 0:
            heapq.heappush(q, c)

print(*answer)