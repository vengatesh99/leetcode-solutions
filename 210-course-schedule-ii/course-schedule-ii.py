class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        for course,pre in prerequisites:
            adj_list[pre].append(course)
        visit = set()
        ans = []
        color = {i:0 for i in range(numCourses)}
        def dfs(node):
            nonlocal ans
            if color[node] == 1:
                return False
            if color[node] == 2:
                return True
            color[node] = 1
            for neib in adj_list[node]:
                if not dfs(neib):
                    return False
            color[node] = 2
            ans.insert(0,node)
            return True
        for i in range(numCourses):
            if color[i] == 0:
                if not dfs(i):
                    return []
        return ans