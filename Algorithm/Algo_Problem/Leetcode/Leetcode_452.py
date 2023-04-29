class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(reverse=True)

        answer = 0
        left, right = -2 ** 31 - 1, -2 ** 31 - 1
        while points:
            l, r = points.pop()

            if l > right:
                answer += 1
                left, right = l, r
            else:
                left, right = max(left, l), min(right, r)

        return answer