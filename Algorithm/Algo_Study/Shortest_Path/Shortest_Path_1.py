# 미래도시

# 해결 방법
# 방문 판매원 A 가 현재 1번에 위치
# X번 회사를 방문해 물건을 파는데 이 때 K번 회사를 거쳐가야함
# Floyd-Warshall 최단거리 알고리즘 이용

# 예시
# 5 7
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4
# 3 5
# 4 5
# 4 5 ==> K = 5, X = 4 이므로 경로를 1번, 3번, 5번, 4번으로 가야 최단거리, 따라서 최단시간: 3

# 풀이
INF = int(1e4)
N, M = map(int, input().split(' '))

# range(N)으로해도 무방
# 그러나 뒤쪽에서 인덱스를 조정할 때 a - 1, b - 1처럼 -1을 해주어야 함
graph = [[INF for _ in range(N + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    graph[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split(' '))
    graph[a][b] = 1
    graph[b][a] = 1

X, K = map(int, input().split(' '))

# Floyd_Warshall 알고리즘 적용
for k in range(1, N + 1):
    for a in range(1, N + 1):
        for b in range(1, N + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = graph[1][K] + graph[K][X]

if answer >= INF:
    print(-1)
else:
    print(answer)