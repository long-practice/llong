# 퀵 정렬
# 시간 복잡도 O(nlog(n))

# 1. 리스트의 첫 번째 데이터를 피벗으로 설정
# 2. 좌측을 두 번째 데이터, 우측을 마지막 데이터로 설정
# 3. 만약 좌측에서 피벗보다 큰 데이터, 우측에서 피벗보다 작은 데이터가 있다면
# 4. 두 데이터 교환
# 5. 좌우측에서 가운데로 범위를 좁혀오면서 계속 진행
# 6. 3의 과정을 거쳤으나 좌측 인덱스가 우측 인덱스보다 클 경우(서로 교차된 경우)
# 7. 우측 인덱스에서 설정한 데이터와 피벗을 교환
# 8. 피벗을 기준으로 좌측, 우측 리스트로 나누어 1 ~ 7의 과정을 반복(재귀 호출)
# 9. 만약 리스트의 크기가 1일 경우 종료

# 피벗을 기준으로 우측 인덱스는 좌우 인덱스가 교차되기 전까지
# 작은 수들을 리스트의 중앙기준(나중에 피벗이 들어갈 자리) 좌측으로 보냄
# 따라서 위의 6의 과정이 성립될 때는 우측 인덱스는 피벗이 들어갈 자리를 지목을 하게 됨
# 예를 들면 크기가 10인 리스트에서 피벗이 리스트에서 5번째로 작은 값이라고 한다면
# 좌우측 인덱스가 교차하여 6의 과정이 성립될 때는 리스트의 5번째의 원소까지는 피벗보다 작은 값이 배치됨
# 즉 [pivot, m1 ~ m4, m6 ~ m10]의 형태로 리스트가 정렬이되게 됨
# 이 상태에서 pivot이 들어갈 자리는 우측 인덱스가 지목한 자리이기 때문에 정렬이 가능함

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8, 4, 8]

def Quick_Sort(arr, start, end):
    if start >= end:
        return
    else:
        left, right = start + 1, end
        pivot = start

        while left <= right:
            while arr[pivot] >= arr[left] and left < end:
                left += 1
            while arr[pivot] <= arr[right] and right > start:
                right -= 1

            if left >= right:
                arr[right], arr[pivot] = arr[pivot], arr[right]
            else:
                arr[left], arr[right] = arr[right], arr[left]

        Quick_Sort(arr, start ,right - 1)
        Quick_Sort(arr, right + 1 ,end)

# 리스트 컴프리핸션을 이용한 파이써닉한 코드
def Quick_Sort_2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]

    left_arr = [x for x in arr[1:] if x < pivot]
    right_arr = [x for x in arr[1:] if x >= pivot]

    return Quick_Sort_2(left_arr) + [pivot] + Quick_Sort_2(right_arr)

# def_Quick_Sort를 이용한 출력방식
# Quick_Sort(array, 0, len(array) - 1)
# print(array)

print(Quick_Sort_2(array))