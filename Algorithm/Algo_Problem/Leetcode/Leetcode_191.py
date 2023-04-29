class Solution:
    def hammingWeight(self, n: int) -> int:
        answer = 0
        for i in range(31, -1, -1):
            if (n >> i) & 1:
                answer += 1
        return answer