# 삽입정렬
# O(n**2)의 시간복잡도
# n회전 시 리스트 내 n + 1번째의 원소를 적절한 위치에 삽입
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# 예시
# 1회전 시 1번째 원소까지는 정렬되었다고 가정, 2번째 원소를 적절한 위치에 삽입
# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# 2회전 시 2번째 원소까지는 정렬되었다고 가정, 3번째 원소를 적절한 위치에 삽입
# array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
# 3회전 시
# array = [0, 5, 7, 9, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0 , -1):
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
        else:
            break
print(array)