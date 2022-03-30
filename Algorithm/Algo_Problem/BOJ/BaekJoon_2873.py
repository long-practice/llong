# 롤러코스터

# 가장 먼저 모든 칸을 방문할 수 있을지에 대한 여부 확인이 필요
# 행 또는 열이 홀수라면 모든 칸을 방문할 수 있으나
# 둘 모두 짝수라면 반드시 최소 한칸은 방문을 못한다고 보면됨

# 예를들어 6 X 6 체스판을 생각해보자
# 좌상단의 영역은 흰색이지만 우하단의 영역또한 흰색
# 대각선의 이동은 허용되지 않으므로 반드시 흰색 -> 검은색 혹은 검은색 -> 흰색으로 이동을하게됨
# 즉 6 X 6 체스판에서의 흰색 영역과 검은색 영역은 각각 18개 이므로
# 반드시 검은색 영역 한 군데는 못 지나가게 됨.(마지막 흰색 영역을 방문할 때 검은색 영역은 17개를 방문하므로)

# 이에 따라 검은색 영역들 중 가장 최소값을 갖는 영역만 방문하지 않으면 됨
import sys
input = sys.stdin.readline

R, C = map(int, input().rstrip().split(' '))
lands = [list(map(int, input().rstrip().split(' '))) for _ in range(R)]
answer = ''

if R % 2:
    answer = ('R' * (C - 1) + 'D' + 'L' * (C - 1) + 'D') * (R // 2) + 'R' * (C - 1)
    print(answer)
elif C % 2:
    answer = ('D' * (R - 1) + 'R' + 'U' * (R - 1) + 'R') * (C // 2) + 'D' * (R - 1)
    print(answer[:-1])
else:
    minimum = 1000
    point = ()
    for r in range(R):
        for c in range(C):
            if (r + c) % 2:
                if minimum > lands[r][c]:
                    minimum = lands[r][c]
                    point = (r, c)

    answer += ('R' * (C - 1) + 'D' + 'L' * (C - 1) + 'D') * (point[0] // 2)
    answer += 'DRUR' * (point[1] // 2)
    if point[1] % 2 == 1:
        answer += 'DR'
    else:
        answer += 'RD'
    answer += 'RURD' * (C // 2 - point[1] // 2 - 1) + 'D'
    answer += ('L' * (C - 1) + 'D' + 'R' * (C - 1) + 'D') * (R // 2 - point[0] // 2 - 1)
    print(answer[:-1])