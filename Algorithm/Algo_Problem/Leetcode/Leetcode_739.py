class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = [(0, temperatures[0])]
        for i in range(1, len(temperatures)):
            while stack and temperatures[i] > stack[-1][1]:
                prev, _ = stack.pop()
                answer[prev] = i - prev
            stack.append((i, temperatures[i]))
        return answer