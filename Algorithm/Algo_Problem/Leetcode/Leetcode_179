class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # nums = list(map(str, nums))
        # nums.sort(key=lambda x: (x*10)[:10])
        # return str(int(''.join(nums[::-1])))
        return str(int(''.join(sorted(list(map(str, nums)), key=lambda x: (x*10)[:10])[::-1])))