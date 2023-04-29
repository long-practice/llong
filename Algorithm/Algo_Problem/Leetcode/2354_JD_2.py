class Solution:
    def countExcellentPairs(self, nums: List[int], k: int) -> int:
        answer = 0
        num_arr = sorted(list(set(nums)), key=lambda x: (bin(x).count('1'), x))
        for i in range(len(num_arr)):
            left, right = i, len(num_arr) - 1
            p = bin(num_arr[left]).count('1')

            while left <= right:
                mid = (left + right) >> 1
                if bin(num_arr[mid]).count('1') + p >= k:
                    right = mid - 1
                else:
                    left = mid + 1

            answer += 2 * (len(num_arr) - left)
            if left == i:
                answer -= 1

        return answer