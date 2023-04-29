class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        answer = ''
        i = 0
        while i < len(num) and int(num[i]) >= change[int(num[i])]:
            answer += num[i]
            i += 1

        while i < len(num) and int(num[i]) <= change[int(num[i])]:
            answer += str(change[int(num[i])])
            i += 1

        return answer + num[i:]
