class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        answer = []
        selected, paths = {}, {}

        for ticket in tickets:
            paths[ticket[0]] = paths.get(ticket[0], []) + [ticket[1]]
            selected[ticket[0]] = selected.get(ticket[0], []) + [False]

        for path_key in paths.keys():
            paths[path_key].sort()

        def get_path(curr, trace):
            if len(trace) == (len(tickets) + 1):
                return trace
            else:
                if curr in paths.keys():
                    for i in range(len(paths[curr])):
                        next_node = paths[curr][i]
                        if not selected[curr][i]:
                            selected[curr][i] = True
                            ans = get_path(next_node, trace + [next_node])
                            if ans:
                                return ans
                            selected[curr][i] = False
            return

        return get_path('JFK', ['JFK'])