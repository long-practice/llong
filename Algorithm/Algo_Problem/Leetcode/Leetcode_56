class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer = []
        intervals.sort()

        left, right = intervals[0]
        for i in intervals:
            if i[0] <= right:
                right = max(right, i[1])
            else:
                answer.append([left, right])
                left, right = i

        answer.append([left, right])
        return answer