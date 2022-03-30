# 간단한 다익스트라 알고리즘
# 그리디 알고리즘의 일종으로 해당 노드에서 다른 노드까지의 거리를 비교했을 때
# 최단 거리인 것만 골라내는 알고리즘
# 간단한 다익스트라 알고리즘의 경우 현재 노드와 연결된 노드를 매번 일일이 확인
# 즉, 매 단계 마다 최단거리 테이블의 모든 원소를 확인 순차 탐색

# 입력 예시
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2

# 출력 예시
# 0
# 2
# 3
# 1
# 2
# 4
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n + 1)]

visited = [False for _ in range(n + 1)]
distance = [INF for _ in range(n + 1)]

# 모든 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split(' '))
    graph[a].append((b, c))

# 방문하지 않은 노드들 중에서 가장 최단 거리 노드의 번호를 반환
def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(len(distance)):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

# 최단 거리 도출
def dijkstra(start):
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]

    for i in range(n - 1):
        now = get_smallest_node()
        visited[now] = True
        for j in graph[now]:
            cost = distance[now] + j[1]
            if cost < distance[j[0]]:
                distance[j[0]] = cost

dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n + 1):
    if distance[i] == INF:
        print("can't go")
    else:
        print("To go ", i, ", You need cost ", distance[i])