class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        char_dict = {s[0]: 1}
        left, right = 0, 1
        answer = 1

        while right < len(s):
            while char_dict.get(s[right], 0):
                char_dict[s[left]] -= 1
                left += 1
            else:
                char_dict[s[right]] = char_dict.get(s[right], 0) + 1
                right += 1
                answer = max(answer, right - left)

        return answer



