# 순차탐색
# 리스트의 데이터 하나씩 접근하면서 특정 문자열과 같은지 검사

def Sequential_Search(array, target):
    for i in range(len(array)):
        if array[i] == target:
            return i
    return -1

input_data = list(input().split(' '))
target_word = input()

# 배열의 인덱스 리턴
print(Sequential_Search(input_data, target_word))