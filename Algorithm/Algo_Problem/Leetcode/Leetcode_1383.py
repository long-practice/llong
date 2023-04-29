class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        answer = 0
        mod = int(1e9) + 7
        arr = sorted(list(zip(efficiency, speed)))

        curr_speed_sum, speed_heap = 0, []
        while arr:
            eff, spd = arr.pop()
            heappush(speed_heap, spd)
            curr_speed_sum += spd

            answer = max(answer, curr_speed_sum * eff)
            if len(speed_heap) == k:
                curr_speed_sum -= heappop(speed_heap)

        return answer % mod