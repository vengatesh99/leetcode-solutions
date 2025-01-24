class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        ans = 0
        for u,v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        def dfs(node,parent):
            nonlocal ans
            max1,max2 =-1,-1
            for neib in adj_list[node]:
                if neib!=parent:
                    m = 1+dfs(neib,node)
                    if m>max1:
                        max1,max2 = m,max1
                    elif m > max2:
                        max2 = m
            ans = max(ans,max1+max2,max1)
            return max(max1,0)
        dfs(0,-1)
        return ans
            