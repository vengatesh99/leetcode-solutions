class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for course,pre in prerequisites:
            adj_list[pre].append(course)
        visit = set()
        def dfs(node):
            if node in visit:
                return False
            if adj_list[node] == []:
                return True
            visit.add(node)
            for neib in adj_list[node]:
                if not dfs(neib):
                    return False
            visit.remove(node)
            adj_list[node] = []
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True