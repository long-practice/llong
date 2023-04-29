class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        answer = 0

        def get_subword(m, nums):
            subword = set()
            window = deque([nums[i] for i in range(m - 1)])

            while m <= len(nums):
                window.append(nums[m - 1])
                subword.add(''.join(window))
                window.popleft()
                m += 1
            return subword

        def check(m):
            s1, s2 = get_subword(m, nums1), get_subword(m, nums2)
            return len(s1 & s2) >= 1

        nums1, nums2 = list(map(str, nums1)), list(map(str, nums2))

        left, right = 0, len(nums2)
        while left <= right:
            mid = (left + right) >> 1

            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right if right > 0 else 0
