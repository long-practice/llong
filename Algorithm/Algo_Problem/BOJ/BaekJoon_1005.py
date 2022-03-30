# ACM Craft

# 풀이 방법
# 그래프의 DFS 탐색을 하듯이 선행 건물을 탐색
# 만약 선행 건물을 이전에 한 번이라도 지었다면(is_made == True)
# DP테이블(building_time)에 저장
# 반복적인 계산을 지양
import sys
input = sys.stdin.readline
sys.setrecursionlimit(int(1e4))

def Build(n):
    # 선행 건물이 있다면
    # 선행 건물 탐색을 하되 각 선행 건물의 건설시간을 time에 저장하여 최댓값을 반환 + 자신 건물의 건설시간을 반환
    if graph[n]:
        time = []
        for g in graph[n]:
            # 이전에 선행건물을 건설한 적이 없으면 탐색(재귀호출)
            if not is_made[g - 1]:
                time.append(Build(g))
            # 이전에 선행건물을 건설을 한 적이 있으면 DP테이블(building_time)에서 값을 가져옴
            else:
                time.append(building_time[g])
        # 자신의 건물 최소 건설시간은 자신의 선행 건물들의 건설시간중 최댓값 + 자신의 건물 건설시간
        building_time[n] += max(time)
    # 건설 처리하여 추후 반복계산 방지
    is_made[n - 1] = True
    return building_time[n]

for _ in range(int(input().rstrip())):
    N, K = map(int, input().rstrip().split(' '))
    graph = [[] for _ in range(N + 1)]
    building_time = [0] + list(map(int, input().rstrip().split(' ')))
    is_made = [False for _ in range(N)]

    for __ in range(K):
        a, b = map(int, input().rstrip().split(' '))
        graph[b].append(a)
    W = int(input().rstrip())

    print(Build(W))