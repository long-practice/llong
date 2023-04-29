class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            left, right = 0, len(word) - 1
            while left <= right:
                if word[left] != word[right]:
                    return False
                left, right = left + 1, right - 1
            return True

        answer = set()
        trie = {'': {}}
        for idx, word in enumerate(words):
            curr, rev_curr = trie[''], trie['']
            for i in range(len(word)):
                if word[i] not in curr.keys():
                    curr[word[i]] = {}
                curr = curr[word[i]]

                if word[-1 - i] not in rev_curr.keys():
                    rev_curr[word[-1 - i]] = {}
                rev_curr = rev_curr[word[-1 - i]]
            curr[0], rev_curr[1] = idx, idx

            # 이게 있으면 시간초과
            # curr = trie['']
            # for i in range(len(word)):
            #     if word[-1 - i] not in curr.keys():
            #         curr[word[-1 - i]] = {}
            #     curr = curr[word[-1 - i]]
            # curr[1] = idx

        def trie_dfs(curr):
            for clf in [0, 1]:
                if clf in curr.keys():
                    tr[clf].append(curr[clf])

            for clf in [0, 1]:
                if clf in curr.keys():
                    idx1 = curr[clf]
                    for idx2 in tr[clf ^ 1]:
                        if idx1 - idx2:
                            if is_palindrome(words[idx1] + words[idx2]):
                                answer.add((idx1, idx2))
                            if is_palindrome(words[idx2] + words[idx1]):
                                answer.add((idx2, idx1))

            for node in curr.keys():
                if node in curr.keys() and node != 0 and node != 1:
                    trie_dfs(curr[node])

            for clf in [0, 1]:
                if clf in curr.keys():
                    tr[clf].pop()

        tr = {0: [], 1: []}
        trie_dfs(trie[''])
        return answer