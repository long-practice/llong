# 커리큘럼

# 입력예시
# 5
# 10 -1
# 10 1 -1
# 4 1 -1
# 4 3 1 -1
# 3 3 -1

# 출력예시
# 10
# 20
# 14
# 18
# 17
from collections import deque

N = int(input())
# 각 강의시간
lecture_time = [0 for _ in range(N + 1)]
# 해당 강의를 들을 때까지 걸리는 시간
total_time = [0 for _ in range(N + 1)]

# 그래프와 진입차수
graph = [[] for _ in range(N + 1)]
indegree = [0 for _ in range(N + 1)]

# 데이터 입력
for i in range(1, N + 1):
    data = list(map(int, input().split()))
    lecture_time[i] = data[0]

    # 그래프 입력, 진입차수 초기화
    for j in range(1, len(data) - 1):
        graph[data[j]].append(i)
        indegree[i] += 1

q = deque()
# 진입차수가 0인 노드 큐에 추가
# 해당 강의는 바로 들을 수 있으므로 강의시간이 총 걸리는 시간과 동일
for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)
        total_time[i] = lecture_time[i]

# 위상정렬
while q:
    curr = q.popleft()

    # 진입차수를 하나씩 줄여가며 큐에 추가
    for g in graph[curr]:
        indegree[g] -= 1
        if indegree[g] == 0:
            # 해당 강의를 들을 때까지 걸리는 시간 = 이전 강의들을 들을 때까지 걸리는 시간들 중 최대값 + 현재 강의를 듣는 시간
            total_time[g] = max(total_time[g], total_time[curr] + lecture_time[g])
            q.append(g)

for i in range(1, N + 1):
    print(total_time[i])