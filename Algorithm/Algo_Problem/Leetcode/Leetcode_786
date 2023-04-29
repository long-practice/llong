class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        h = []
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if len(h) < k:
                    heapq.heappush(h, (-arr[i] / arr[j], arr[i], arr[j]))
                else:
                    if h[0][0] < -arr[i] / arr[j]:
                        heapq.heappushpop(h, (-arr[i] / arr[j], arr[i], arr[j]))
                    else:
                        continue
        return h[0][1], h[0][2]

