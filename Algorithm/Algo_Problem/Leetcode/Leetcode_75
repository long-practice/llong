class Solution:
    def sortColors(self, nums: List[int]) -> None:
        array = [0 for _ in range(3)]
        for n in nums:
            array[n] += 1

        nums.clear()
        for i in range(3):
            nums += [i] * array[i]