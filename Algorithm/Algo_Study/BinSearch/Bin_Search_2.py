# 떡볶이 떡 만들기

# 해결방법
# 떡의 개수가 최대 100만개, 최대 길이가 20억이므로 순차 탐색의 경우에 소요 시간이 길어질 수 있음. 따라서 이진탐색 이용
# 1. start = 1, end = max(array)로 설정하여 이진탐색 시작
# 2. mid 값을 기준으로 떡을 자르고 남은 떡의 양을 모두 더해주기
# 3. 더한 떡의 양이 M보다 작으면 end 값을 mid - 1로 수정 탐색 시작
# 4. 만약 더한 떡의 양이 M보다 크면 start 값을 mid + 1로 수정 후 탐색 시작
# 5. 이진 탐색 조건이 가능할 때까지 탐색, 마지막으로 가능했던 mid값이 정답

N, M = map(int, input().split(' '))
length = list(map(int, input().split(' ')))

# 1. start = 1, end = max(array)로 설정
start, end = 1, max(length)
answer = 0

# 이진 탐색 시작
while start <= end:
    total = 0
    # 2. mid 값을 기준으로 떡을 자르고 남은 떡의 양을 모두 더해주기
    mid = (start + end) // 2

    for l in length:
        if l > mid:
            total += l - mid
    # 3. 더한 떡의 양이 M보다 작으면 mid값 수정
    # 4. 더한 떡의 양이 M보다 크면 start 값을 mid + 1로 탐색
    if total >= M:
        start = mid + 1
        # 5. start > end가 될 때 이진탐색 종료
        # 이 때 answer 값이 남은 떡의 양이 M보다 큰 조건을 만족하는 최대값
        answer = mid
    else: # total < M:
        end = mid - 1

print(answer)