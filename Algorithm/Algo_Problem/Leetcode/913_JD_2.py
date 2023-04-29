class Solution(object):
    def catMouseGame(self, graph):
        MOUSE, CAT, DRAW = 1, 2, 0
        N = len(graph)

        def get_parents(mouse, cat, turn):
            if turn == CAT:
                for mouse_prev in graph[mouse]:
                    yield mouse_prev, cat, MOUSE
            else:
                for cat_prev in graph[cat]:
                    if cat_prev != 0:
                        yield mouse, cat_prev, CAT

        degree = dict()
        for m in range(N):
            for c in range(N):
                degree[m, c, 1] = len(graph[m])
                degree[m, c, 2] = len(graph[c]) - (0 in graph[c])

        colors = collections.defaultdict(int)
        queue = collections.deque([])

        for turn in [MOUSE, CAT]:
            for i in range(N):
                colors[0, i, turn] = MOUSE
                queue.append((0, i, turn, MOUSE))
                if i > 0:
                    colors[i, i, turn] = CAT
                    queue.append((i, i, turn, CAT))

        while queue:
            mouse, cat, turn, color = queue.popleft()
            for mouse_prev, cat_prev, turn_prev in get_parents(mouse, cat, turn):
                if colors[mouse_prev, cat_prev, turn_prev] == DRAW:
                    if color == turn_prev:
                        colors[mouse_prev, cat_prev, turn_prev] = color
                        queue.append((mouse_prev, cat_prev, turn_prev, color))
                    else:
                        degree[mouse_prev, cat_prev, turn_prev] -= 1
                        if not degree[mouse_prev, cat_prev, turn_prev]:
                            colors[mouse_prev, cat_prev, turn_prev] = 3 - turn_prev
                            queue.append((mouse_prev, cat_prev, turn_prev, 3 - turn_prev))

        return colors[1, 2, 1]