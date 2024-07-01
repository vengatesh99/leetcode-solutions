class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        topo_sort = []
        is_possible = True
        color = {k:Solution.WHITE for k in range(numCourses)}
        
        def dfs(start):
            nonlocal is_possible

            if not is_possible:
                return
            color[start] = Solution.GRAY
            for neib in adj_list[start]:
                if color[neib] == Solution.WHITE:
                    dfs(neib)
                elif color[neib] == Solution.GRAY:
                    is_possible = False
            color[start] = Solution.BLACK
            topo_sort.append(start)
        
        adj_list = defaultdict(list)
        for arr in prerequisites:
            adj_list[arr[1]].append(arr[0])
        for i in range(numCourses):
            if color[i] == Solution.WHITE:
                dfs(i)
        return topo_sort[::-1] if is_possible else []
