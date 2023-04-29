class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) >> 1
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        pivot = right

        def bisect(left, right, trg):
            while left <= right:
                mid = (left + right) >> 1
                if nums[mid] < trg:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        l, r = bisect(0, pivot - 1, target), bisect(pivot, len(nums) - 1, target)

        if nums[l] == target:
            return l
        elif r < len(nums) and nums[r] == target:
            return r
        else:
            return -1