# 공항

# 트리 자료구조 이용(union-find 알고리즘 일부)
# 게이트의 값이 가능한 큰 순서대로 비행기를 도킹시키되
# 순차탐색으로 가능한 게이트를 찾아내는 것이 아닌
# 트리 자료구조의 부모노드를 참조함으로써 도킹가능한 게이트를 찾아내기

# find함수를 주목하고 코드가 작동하는 방식은 암기할 것

import sys
sys.setrecursionlimit(int(1e5))

G = int(sys.stdin.readline().rstrip())
gate = [x for x in range(0, G + 1)]

def find(x):
    if x == gate[x]:
        gate[x] = x - 1
        return x - 1
    else:
        y = find(gate[x])
        gate[x] = y
        return y

# 입력을 그때그때 받아서 바로바로 공항에 오는 비행기가 도킹이 가능한지 확인
# 몇몇 문제에서는 입력을 전부 받지 않으면 틀렸다고 하므로 권장하지는 않음
answer = 0
for _ in range(int(sys.stdin.readline().rstrip())):
    a = int(sys.stdin.readline().rstrip())
    P = find(a)
    answer += 1
    if gate[a] == -1:
        print(answer - 1)
        break
else:
    print(answer)
