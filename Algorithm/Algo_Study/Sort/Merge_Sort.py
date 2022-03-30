# 병합정렬
# 시간 복잡도 O(nlog(n))

# 1. 리스트를 반으로 쪼개 나가면서 길이가 1인 리스트로 분할
# 2. 인접한 두 개의 리스트를 하나로 병합해나가면서 정렬

# 예시
# [5, 7, 9, 0, 3, 1, 6, 2, 4, 8, 4, 8]

# 분할과정
# [5, 7, 9, 0, 3, 1], [6, 2, 4, 8, 4, 8]
# [5, 7, 9], [0, 3, 1], ...
# [5, 7], [9], [0, 3], [1], ...
# [5], [7], [9], [0], [3], [1], ...

# 병합과정
# [5, 7], [9]
# [5, 7, 9], [0], [3], [1], ...
# [5, 7, 9], [0, 3], [1], ...
# [5, 7, 9], [0, 1, 3], ...
# [0, 1, 3, 5, 7, 9], [2, 4, 4, 6, 8, 8]
# [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9]

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8, 4, 8]

def Merge_Sort(arr):
    if len(arr) <= 1:
        return arr
    mid = (len(arr) - 1) // 2

    # 리스트 분할
    left_arr = Merge_Sort(arr[:mid + 1])
    right_arr = Merge_Sort(arr[mid + 1:])

    left_idx, right_idx = 0, 0
    merge_arr = []

    # 리스트 병합
    while left_idx < len(left_arr) and right_idx < len(right_arr):
        if left_arr[left_idx] <= right_arr[right_idx]:
            merge_arr.append(left_arr[left_idx])
            left_idx += 1
        else: # left_arr[left_idx] > right_arr[right_idx]:
            merge_arr.append(right_arr[right_idx])
            right_idx += 1

    while left_idx < len(left_arr):
        merge_arr.append(left_arr[left_idx])
        left_idx += 1
    while right_idx < len(right_arr):
        merge_arr.append(right_arr[right_idx])
        right_idx += 1

    return merge_arr

Sort_array = Merge_Sort(array)
print(Sort_array)