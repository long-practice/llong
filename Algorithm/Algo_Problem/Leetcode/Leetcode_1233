class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        answer = []

        trie = {}
        for f in folder:
            f_ls = f.split('/')
            curr = trie
            for sub_f in f_ls:
                if sub_f not in curr.keys():
                    curr[sub_f] = {}
                curr = curr[sub_f]
            curr['/'] = f

        def search(curr):
            if '/' in curr.keys():
                answer.append(curr['/'])
                return

            for t in curr.keys():
                if t != '/':
                    search(curr[t])

        search(trie)
        return answer