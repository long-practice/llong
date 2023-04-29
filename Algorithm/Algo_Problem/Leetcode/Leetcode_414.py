class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        h = []
        for n in set(nums):
            if len(h) < 3:
                heappush(h, n)
            else:
                heappushpop(h, n)

        return min(h) if len(h) == 3 else max(h)