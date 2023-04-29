class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        answer = 0
        count = [0 for _ in range(31)]
        for n in set(nums):
            count[bin(n).count('1')] += 1

        count = list(accumulate(count))
        for i in range(1, 31):
            answer += (count[i] - count[i - 1]) * (count[-1] - count[min(max(k - i - 1, 0), 30)])

        return answer
