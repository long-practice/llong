# 위상 정렬

# 진입 차수를 저장할 테이블을 만들고 매 순간 진입 차수가 0인 노드를 큐에 삽입
# 다른 노드와 연결된 간선을 하나씩 끊어가며 진입 차수 테이블을 갱신

# 입력예시
# 7 8
# 1 2
# 1 5
# 2 3
# 2 6
# 3 4
# 4 7
# 5 6
# 6 4

# 출력예시
#1 2 5 3 6 4 7

from collections import deque

v, e = map(int, input().rstrip().split(' '))
indegree = [0 for _ in range(v + 1)]
graph = [[] for _ in range(v + 1)]

for _ in range(e):
    a, b = map(int, input().rstrip().split(' '))
    graph[a].append(b)
    # a에서 b로 연결되었으니 b의 진입차수 1증가
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    # 최초 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        curr = q.popleft()
        result.append(curr)

        # 현재 노드와 연결된 노드의 진입차수를 1씩 줄이기
        for g in graph[curr]:
            indegree[g] -= 1
            if indegree[g] == 0:
                q.append(g)
    return result

print(*topology_sort())