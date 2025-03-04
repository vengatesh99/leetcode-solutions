class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        pq = []
        mp = Counter(arr)
        for key,v in mp.items():
            heapq.heappush(pq,(v,key))
        while k>0 and pq:
            v,key = heapq.heappop(pq)
            if v-k>0:
                heapq.heappush(pq,(v-k,key))
            k = k-v
        return len(pq)
                