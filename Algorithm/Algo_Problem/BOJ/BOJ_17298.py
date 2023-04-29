import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
answer = [-1 for _ in range(N)]
stack = []

for i in range(N):
    while stack and nums[stack[-1]] < nums[i]:
        idx = stack.pop()
        answer[idx] = nums[i]
    stack.append(i)
print(*answer)