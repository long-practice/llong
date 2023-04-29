class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        answer = 0

        curr = prices[0]
        for i in range(len(prices)):
            if prices[i] > curr:
                answer += prices[i] - curr
            curr = prices[i]

        return answer
