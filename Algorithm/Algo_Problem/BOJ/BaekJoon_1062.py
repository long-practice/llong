# 가르침

# 문자열을 입력 받은 후 배워야할 문자들을 따로 분리시킴, 배워야할 문자들을 비트 값으로 변환하여 저장
# 만약 어떤 단어에 대해 배워야할 문자가 없다면 그 단어는 무조건 읽을 수 있고, 배워야할 문자가 K - 5보다 많다면 그 단어는 읽을 수 없음
# 최초에 배울 수 있는 문자가 5보다 작다면 읽을 수 있는 단어는 없음
# 배울 수 있는 문자가 5이상 이면서 배워야할 문자의 수가 배울 수 있는 문자의 수보다 작다면 모든 단어를 읽을 수 있음

# 배워야할 문자들에 대해 비트화를 해주고 조합 생성
# 각 단어에서 배워야할 문자들과 배운 문자조합과의 비트마스킹
# 비트마스킹 결과 값이 각 단어에서 배워야할 문자들과 동일하다면 그 단어는 읽을 수 있음

import sys
from itertools import combinations
def input():
    return sys.stdin.readline().rstrip('\n')

N, K = map(int, input().split(' '))
words = []
learn = set()
char_dict = {chr(ord('a') + i) : 1 << i for i in range(26)}
knowing = set("antic")
count, answer = 0, 0

for _ in range(N):
    temp = set(input().rstrip("tica").lstrip("anta")) - knowing
    if len(temp) == 0:
        count += 1
    elif len(temp) <= K - 5:
        bit_value = 0
        for v in temp:
            bit_value += char_dict[v]
        words.append(bit_value)
        learn |= temp

if K < 5:
    print(0)
else:
    if len(learn) <= K - 5:
        print(len(words) + count)
    else:
        learn = [char_dict[c] for c in learn]
        for have_learned in combinations(learn, K - 5):
            mask = sum(have_learned)
            ans = count
            for word_value in words:
                if word_value & mask == word_value:
                    ans += 1
            answer = ans if ans > answer else answer
        print(answer)