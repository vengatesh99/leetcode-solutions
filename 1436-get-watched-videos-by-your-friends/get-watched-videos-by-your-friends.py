class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        adj_list = {}
        n = len(watchedVideos)
        for i,friend in enumerate(friends):
            adj_list[i] = friend
        q = deque()
        q.append(id)
        visit = set()
        visit.add(id)
        hashmap = defaultdict(int)
        while q and level:
            sz = len(q)
            while sz and q:
                node = q.popleft()
                for neib in adj_list[node]:
                    if neib not in visit:
                        q.append(neib)
                        visit.add(neib)
                sz-=1
            level-=1
        while q:
            node = q.popleft()
            for vid in watchedVideos[node]:
                hashmap[vid]+=1
            if node in visit:
                continue
            visit.add(node)
        return sorted(hashmap.keys(), key = lambda x: (hashmap[x],x))
