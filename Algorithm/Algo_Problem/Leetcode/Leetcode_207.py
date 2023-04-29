class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for req in prerequisites:
            if req[1] != req[0]:
                graph[req[1]].append(req[0])
            else:
                return False
        visited = [False for _ in range(numCourses)]

        def dfs(curr, trace):
            visited[curr] = True
            for g in graph[curr]:
                if g in trace or (not visited[g] and not dfs(g, trace + [curr])):
                    return False
            return True

        for course in range(numCourses):
            if not visited[course] and not dfs(course, []):
                return False

        return True