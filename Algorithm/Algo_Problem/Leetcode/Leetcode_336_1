class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            left, right = 0, len(word) - 1
            while left <= right:
                if word[left] != word[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        answer = []
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if is_palindrome(words[i] + words[j]):
                    answer.append([i, j])
                if is_palindrome(words[j] + words[i]):
                    answer.append([j, i])
        return answer
