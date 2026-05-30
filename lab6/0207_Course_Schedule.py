class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        for crs, pre in prerequisites:
            graph[pre].append(crs)
        visit = [0] * numCourses

        def dfs(crs):
            if visit[crs] == 1:
                return False
            if visit[crs] == 2:
                return True
            visit[crs] = 1

            for next_crs in graph[crs]:
                if not dfs(next_crs):
                    return False
            visit[crs] = 2
            return True

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True