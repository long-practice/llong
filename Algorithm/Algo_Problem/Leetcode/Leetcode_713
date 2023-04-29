class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        answer = 0

        left, right = 0, 0
        v = 1
        for i in range(len(nums)):
            v *= nums[i]
            right = i
            while v >= k and left <= right:
                v //= nums[left]
                left += 1
            answer += right - left + 1

        return answer
