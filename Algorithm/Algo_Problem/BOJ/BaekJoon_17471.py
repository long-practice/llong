# 게리맨더링

# step1. 입력, 문제상황 구현, 인접리스트 표현
# step2. n C (1 ~ n - 1)로 노드를 선택하여 하나의 group 생성 나머지 노드들로 또 다른 group 생성
# step3. 각 그룹이 유효한지 확인(인접한 노드들인지 확인)
# function1. dfs 진행 함수
# step4. 매 단계에서 인구의 차이를 구하기
# step5. 만약 매 단계에서 인구의 차이를 못하고(각 그룹이 유효하지 않아서) 출력이 INF라면 -1반환

# step1
import sys
from itertools import combinations

N = int(sys.stdin.readline().rstrip('\n'))
people = list((map(int, sys.stdin.readline().rstrip('\n').split(' '))))
graph = [[]]
for i in range(1, N + 1):
    graph.append(list(map(int, sys.stdin.readline().rstrip('\n').split(' ')))[1:])

# function1
def func1(graph, group, visited, curr, count):
    visited[curr] = True
    count += 1
    for next_node in graph[curr]:
        if next_node in group and not visited[next_node]:
            func1(graph, group, visited, next_node, count)

INF = 1000
answer = INF

# step2
for n in range(1, N // 2 + 1):
    for nodes in combinations([x for x in range(1, N + 1)], n):
        group_2 = [x for x in nodes]
        group_1 = [x for x in range(1, N + 1) if x not in group_2]

        # step3
        visited = [False for _ in range(N + 1)]
        func1(graph, group_1, visited, group_1[0], 0)
        is_valid_group_1 = all([visited[x] for x in group_1])

        visited = [False for _ in range(N + 1)]
        func1(graph, group_2, visited, group_2[0], 0)
        is_valid_group_2 = all([visited[x] for x in group_2])

        # step4
        if is_valid_group_1 and is_valid_group_2:
            answer = min(answer, abs(sum([people[x - 1] for x in group_1]) - sum([people[x - 1] for x in group_2])))
        else:
            continue

# step5
if answer == INF:
    print(-1)
else:
    print(answer)