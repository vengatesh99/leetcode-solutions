class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        for s,d,w in roads:
            graph[s].append((d,w))
            graph[d].append((s,w))
        print(graph)
        def dfs(node):
            if node in visited:
                return float("inf")
            visited.add(node)
            weight = float("inf")
            for neib,w in graph[node]:
                weight = min(weight,w,dfs(neib))
            return weight
        ans = dfs(1)
        print(visited)
        return ans
