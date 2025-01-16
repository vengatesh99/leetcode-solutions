class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        visit = set()
        for i in range(len(rooms)):
            for key in rooms[i]:
                adj_list[i].append(key)
        def dfs(node):
            visit.add(node)
            for neib in adj_list[node]:
                if neib not in visit:
                    dfs(neib)
        dfs(0)
        return len(visit) == len(rooms)
