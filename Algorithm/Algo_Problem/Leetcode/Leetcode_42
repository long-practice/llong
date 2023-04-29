class Solution:
    def trap(self, height: List[int]) -> int:
        answer, stack = 0, []
        for w in range(len(height)):
            while stack and stack[-1][1] <= height[w]:
                prev_w, prev_h = stack.pop()
                if stack:
                    w_len = w - stack[-1][0] - 1
                    h_len = min(stack[-1][1], height[w]) - prev_h
                    answer += w_len * h_len
            stack.append((w, height[w]))
        return answer