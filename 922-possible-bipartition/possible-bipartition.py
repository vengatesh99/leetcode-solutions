class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        start = -1
        visit = defaultdict(int)
        for u,v in dislikes:
            adj_list[u].append(v)
            adj_list[v].append(u)
        for node in range(1,n+1):
            if node in visit:
                continue
            queue = [(node,1)]
            while queue:
                node,color = queue.pop(0)
                if node in visit:
                    if visit[node] != color:
                        return False
                    continue
                visit[node] = color
                for neib in adj_list[node]:
                    if neib not in visit:
                        queue.append((neib,not color))
        return True
                

        