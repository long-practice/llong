class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        num_in_window = [0 for _ in range(int(2e4) + 1)]

        h = []
        for i in range(k):
            if not num_in_window[nums[i]]:
                heapq.heappush(h, -nums[i])
            num_in_window[nums[i]] += 1
        answer.append(-h[0])

        left, right = 0, k
        while right < len(nums):
            l, r = nums[left], nums[right]
            if not num_in_window[r]:
                heapq.heappush(h, -r)
            num_in_window[r] += 1

            num_in_window[l] -= 1
            while not num_in_window[-h[0]]:
                heapq.heappop(h)

            answer.append(-h[0])
            left, right = left + 1, right + 1

        return answer



