class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        answer = 0

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        for i in range(2 * (len(nums2) - 1) + (len(nums1) - len(nums2) + 1)):
            left, right = max(0, len(nums2) - 1 - i), min(len(nums2), len(nums1) - i - 1 + len(nums2))

            a, flag, count = 0, False, 0
            while a < right - left:
                if nums2[left + a] == nums1[max(i + 1 - len(nums2), 0) + a]:
                    count += 1
                    flag = True
                else:
                    if flag:
                        answer = max(answer, count)
                        flag = False
                    count = 0
                a += 1
            answer = max(answer, count)

        return answer
