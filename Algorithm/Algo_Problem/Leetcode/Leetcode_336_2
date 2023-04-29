class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(word):
            left, right = 0, len(word) - 1
            while left <= right:
                if word[left] != word[right]:
                    return False
                left, right = left + 1, right - 1
            return True


        def trie_dfs(node_dict, trace):
            if '/' in node_dict.keys():
                idx1 = node_dict['/']

                tr_idx, idx2_ls = 0, []
                rev_curr = rev_trie['']
                while tr_idx < len(trace):
                    if '/' in rev_curr.keys():
                        idx2_ls.append(rev_curr['/'])

                    rev_node = trace[tr_idx]
                    if rev_node in rev_curr.keys():
                        rev_curr = rev_curr[rev_node]
                        tr_idx += 1
                    else:
                        break
                else:
                    idx2_ls += rev_trie_dfs(rev_curr, [])

                for idx2 in idx2_ls:
                    if idx1 - idx2 and is_palindrome(words[idx1] + words[idx2]):
                        answer.append([idx1, idx2])

            for node in node_dict.keys():
                if node != '/':
                    trie_dfs(node_dict[node], trace + [node])


        def rev_trie_dfs(node_dict, rev_words_ls):
            if '/' in node_dict.keys():
                rev_words_ls.append(node_dict['/'])

            for node in node_dict.keys():
                if node != '/':
                    rev_words_ls = rev_trie_dfs(node_dict[node], rev_words_ls)

            return rev_words_ls


        answer = []
        trie, rev_trie = {'': {}}, {'': {}}

        for idx, word in enumerate(words):
            curr, rev_curr = trie[''], rev_trie['']
            for i in range(len(word)):
                if word[i] not in curr.keys():
                    curr[word[i]] = {}
                if word[-1 - i] not in rev_curr.keys():
                    rev_curr[word[-1 - i]] = {}
                curr, rev_curr = curr[word[i]], rev_curr[word[-1 - i]]
            curr['/'], rev_curr['/'] = idx, idx

        trie_dfs(trie[''], [])
        return answer