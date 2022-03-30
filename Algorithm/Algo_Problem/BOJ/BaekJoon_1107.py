# 리모컨

# # 입력
# # target_len 변수는 target의 자릿수
# target = int(input())
# target_len = len(str(target))
#
# # 고장난 버튼 입력
# # available은 사용가능한 버튼만 모아서 정렬한 리스트
# # 고장난 버튼이 없으면 입력 받지 않음
# error = int(input())
# available = [str(x) for x in range(10)]
# if error > 0:
#     available = list(set(available) - set([x for x in input().split(' ')]))
# available.sort()
#
#
# # 나중에 본문에서 함수 실행 전후로 target_len - 1의 자릿수를 가지는 채널의 최대값과(1)
# # target_len + 1의 자릿수를 가지는 채널의 최소값을 channels에 저장(2)
# # (1) 만약 target이 1001일 때 999 + 2로 접근하는 것이 이득
# # (2) 만약 target이 999일 때 1000 - 1로 접근하는 것이 이득
#
# # 사용가능한 버튼으로 target의 자릿수만큼 조합할 수 있는 채널에서 target으로 접근하는 함수
# def get_value(c, avail):
#     global target, min_count
#     if len(c) == len(str(target)):
#         min_count = min(min_count, len(c) + abs(int(c) - target))
#         return min_count
#     else:
#         for i in avail:
#             c += i
#             min_count = get_value(c, avail)
#             c = c[:-1]
#     return min_count
#
# # +, -로 target채널에 접근할 경우
# if len(available) == 0:
#     print(abs(target - 100))
#
# # available에 0만 있는 경우에는 0입력 후 +로 target채널에 접근
# # 혹은 100에서 -로 접근
# elif available == ['0']:
#     if abs(target - 100) > target + 1:
#         print(target + 1)
#     else:
#         print(abs(target - 100))
#
# # 이 외의 경우
# # min_count의 초기값은 target 채널을 +, -만을 이용하여 접근할 때의 값
# else:
#     # print('available ', available)
#     min_count = abs(target - 100)
#
#     # print('1 ', min_count)
#     # 위에서 설명한 (1)의 경우
#     if target >= 10:
#         min_count = min(min_count, (target_len - 1) + abs(target - int(available[-1] * (target_len - 1))))
#     # print('2 ', min_count)
#     # target_len 자릿수 만큼 조합할 수 있는 채널에서 target 접근할 경우
#     for a in available:
#         min_count = min(min_count, get_value(a, available))
#     # print('3 ', min_count)
#     # 위에서 설명한 (2)의 경우
#     # 위의 (2)의 경우를 만족하는 수를 구할 때 available의 최소값으로 target + 1 크기만큼 도핑하여 구할 수 있음
#     # 그러나 available의 최소값이 0이라면 경우가 다름
#     # 두번 째로 작은 available값 뒤에 0을 target_len만큼 도핑해주어야 함
#     if available[0] == '0':
#         min_count = min(min_count, (target_len + 1) + abs(int(available[1] + available[0] * target_len) - target))
#     else:
#         min_count = min(min_count, (target_len + 1) + abs(int(available[0] * (target_len + 1)) - target))
#     # print('4 ', min_count)
#     # 조합한 채널들로 반복문 수행
#     # count = {채널 입력(자릿수 만큼)} + {해당 채널과 target 채널과의 차이만큼 "+-" 수행}
#     # 만약 이전 min_count가 count 보다 크면 min_count값 수정
#     print(min_count)



def sol1107():
    n = int(input())
    m = int(input())
    c = list(str(i) for i in range(10))
    if m > 0:
        for i in input().split():
            c.remove(i)
    if len(c) == 0:
        return abs(n - 100)

    s = len(str(n))
    words = []
    for i in range(len(c)):
        words.append(c[i])
    if c[0] != "0" or len(c) > 1:
        words.append((c[0] if c[0] != "0" else c[1]) + c[0])
    if s > 1:
        words.append("")

    vals = []
    count = 1
    while count < s:
        vals.clear()
        for w in words:
            x = int(w + c[0] * (s - count))
            vals.append((abs(n - x) + len(str(x)), w))
        vals.sort()
        words.clear()
        if len(vals) == 1:
            for i in range(len(c)):
                words.append(vals[0][1] + c[i])
        else:
            for i in range(len(c)):
                words.append(vals[0][1] + c[i])
                words.append(vals[1][1] + c[i])
        count += 1
    vals.clear()
    for w in words:
        x = int(w)
        vals.append(abs(n - x) + len(str(x)))
    return min(abs(n - 100), min(vals))

print(sol1107())