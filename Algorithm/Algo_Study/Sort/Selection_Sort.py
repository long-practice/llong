# 선택정렬
# O(n**2)의 시간복잡도
# n회전 시 리스트 내 n번째로 작은 값을 리스트의 n번째 원소에 배치시킴
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 예시
# 1회전 시
# array = [0, 5, 9, 7, 3, 1, 6, 2, 4, 8]
# 2회전 시
# array = [0, 1, 9, 7, 3, 5, 6, 2, 4, 8]

for i in range(len(array) - 1):
    min_value_idx = i
    for j in range(i + 1, len(array)):
        if array[min_value_idx] > array[j]:
            min_value_idx = j
    array[i], array[min_value_idx] = array[min_value_idx], array[i]
print(array)