class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        answer = 0

        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1

        nums1, nums2 = deque(nums1), deque(nums2)
        for _ in range(len(nums2) - 1):
            nums1.appendleft(-1)
            nums1.append(-1)
        nums1.appendleft(-1)

        for i in range(len(nums1) - len(nums2)):
            nums1.popleft()
            count, flag = 0, False
            for j in range(len(nums2)):
                if nums1[j] == nums2[j]:
                    if not flag:
                        flag = True
                    count += 1
                else:
                    count, flag = 0, False
                answer = max(answer, count)

        return answer
