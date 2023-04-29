class Solution:
    def catMouseGame(self, graph) -> int:
        res = [[[3 for _ in range(len(graph))] for _ in range(len(graph))] for _ in range(2)]
        result = {'mouse_win': 1, 'cat_win': 2, 'draw': 0}

        for a in range(2):
            for b in range(len(graph)):
                for d in range(len(graph)):
                    if b == 0:
                        res[a][b][d] = result['mouse_win']
                    elif b == d:
                        res[a][b][d] = result['cat_win']

        def move_mouse(m, c, turn):
            t = turn % 2
            print('mouse:', m, 'cat:', c, 'turn:', 'mouse' if not t else 'cat', f'({turn})')
            if turn == 101:
                res[t][m][c] = 0
            if res[t][m][c] == 3:
                r = 2
                for g in graph[m]:
                    # if turn == 101:
                    #     res[t^1][m][c] = 0
                    #     return 0
                    # else:
                    r = move_cat(g, c, turn + 1)

                    # 쥐의 입장에서 현재 고양이가 어떻게든 움직여도 쥐가 이기면 현재 수가 최선의 수
                    if r == result['mouse_win']:
                        break
                    else:
                        r = min(res[t][m][c], r)

                print(f'update res[{t}][{m}][{c}]', res[t][m][c], 'to', r)
                res[t][m][c] = r
            return res[t][m][c]

        def move_cat(m, c, turn):
            t = turn % 2
            print('mouse:', m, 'cat:', c, 'turn:', 'mouse' if not t else 'cat', f'({turn})')
            if turn == 101:
                res[t][m][c] = 0
            if res[t][m][c] == 3:
                r = 1
                for g in graph[c]:
                    if g:
                        # if turn == 101:
                        #     print(turn)
                        #     res[t^1][m][c] = 0
                        #     return 0
                        # else:
                        r = move_mouse(m, g, turn + 1)

                    if r == result['cat_win']:
                        break
                    else:
                        r = min(res[t][m][c], r)

                print(f'update res[{t}][{m}][{c}]', res[t][m][c], 'to', r)
                res[t][m][c] = r
            return res[t][m][c]

        # 쥐부터 시작 (mouse, cat, turn)
        ans = move_mouse(1, 2, 0)
        from pprint import pprint
        pprint(res)

        return ans
        # return move_mouse(1, 2, 0)

# print(Solution().catMouseGame([[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]))
# print(Solution().catMouseGame([[1,3],[0],[3],[0,2]]))
print(Solution().catMouseGame([[2,6],[2,4,5,6],[0,1,3,5,6],[2],[1,5,6],[1,2,4],[0,1,2,4]]))