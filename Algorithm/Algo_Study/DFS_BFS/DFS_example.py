# DFS 예제

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
# 노드별 내림차순 정렬, 최소 노드 우선 방문 위함
for g in graph:
    g.sort(reverse=True)

# 스택으로 구현
stack = []

# 방문처리 선형 배열
visited = [False for _ in range(len(graph))]

# 시작 노드
start = 1

answer = []

# 최초 상태 설정
# 출발 노드에 대해 방문처리, 스택과 이동 경로에 추가
visited[start] = True
stack.append(start)
answer.append(start)

# 스택이 비어있을 때 까지 탐색
# 현재 상태에서 스택 최상단에 있는 노드를 기준으로 다음으로 방문할 노드를 탐색
# 만약 다음으로 방문할 노드가 없을 경우
# 이전으로부터 왔던 경로를 되돌아가야함. 스택의 pop연산으로 구현
while len(stack) > 0:
    curr = stack[-1]
    # 다음으로 방문할 노드가 있을 때 까지 탐색
    # 다음으로 방문할 노드가 이전에 방문하지 않았다면
    # 현재 위치를 해당 노드로 변경, 스택 및 경로에 추가, 방문 처리
    # 해당 노드를 방문한 적이 있다면 그래프 경로 리스트에 pop연산, 다음 노드 탐색
    while len(graph[curr]) > 0:
        if not visited[graph[curr][-1]]:
            curr = graph[curr].pop()
            stack.append(curr)
            answer.append(curr)
            visited[curr] = True
        else:
            graph[curr].pop()
    stack.pop()
print(answer)