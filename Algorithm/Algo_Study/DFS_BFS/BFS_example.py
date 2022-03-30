# BFS 예제
from collections import deque

def BFS(graph, init, visited):
    # 방문처리 및 해당 노드 출력
    visited[init] = True

    # 큐 자료구조 이용
    queue = deque([init])

    # 큐가 빌 때까지 반복문 진행
    # 큐에서 노드를 반환하고 출력
    # 해당 노드와 연결되어 있는 다른 노드들에 대해서 방문한 적이 없다면
    # 큐에 다른 노드들을 삽입(숫자가 낮은 노드들과 연결된 노드들을 우선적으로 삽입), 방문 처리
    while queue:
        curr = queue.popleft()
        print(curr, end = ' ')
        for g in graph[curr]:
            if not visited[g]:
                queue.append(g)
                visited[g] = True

# 그래프 구현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 방문처리 선형 배열
visited = [False for _ in range(len(graph))]
# 시작 노드
start = 1
# DFS 시작
BFS(graph, start, visited)