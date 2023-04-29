class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
        def func(d):
            return 2 * d * (d + 1) * (2 * d + 1)

        left, right = 0, 62995
        while left <= right:
            mid = (left + right) >> 1

            if func(mid) < neededApples:
                left = mid + 1
            else:
                right = mid - 1

        return 8 * left