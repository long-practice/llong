class Solution:
    def numSplits(self, s: str) -> int:
        answer = 0
        left, right = set(), set(s)
        count_dict = Counter(s)

        i = 0
        while len(left) <= len(right):
            c = s[i]
            left.add(c)
            count_dict[c] -= 1
            if not count_dict[c]:
                right.remove(c)
            if len(left) == len(right):
                answer += 1
            i += 1

        return answer