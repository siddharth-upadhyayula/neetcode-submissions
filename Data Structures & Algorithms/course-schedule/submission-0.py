class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        for i in range(numCourses):
            graph[i]=[]
        for i, pre in prerequisites:
            graph[pre].append(i)

        visited = set()
        visiting = set()

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for i in graph[course]:
                if not dfs(i):
                    return False
            
            visiting.remove(course)
            visited.add(course)

            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True 