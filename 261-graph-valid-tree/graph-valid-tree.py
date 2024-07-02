class Solution:
    WHITE = 1
    GRAY = 2
    BLACK = 3
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        color = {k:Solution.WHITE for k in range(n)}
        adj_list = defaultdict(list)
        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def dfs(node,parent):
            if color[node] == Solution.GRAY:
                return False
            color[node] = Solution.GRAY
            if node in adj_list:
                for neib in adj_list[node]:
                    if neib == parent:
                        continue
                    if not dfs(neib,node):
                        print(node,neib)
                        return False
                color[node] = Solution.BLACK
            return True
        component = False
        for vertex in range(n):
            if color[vertex] == Solution.WHITE:
                if component or not dfs(vertex,vertex):
                    return False
                component = True
        return True        
