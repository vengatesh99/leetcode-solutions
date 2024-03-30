class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = Counter(nums)
        arr = [(v,k) for k,v in my_dict.items()]
        heapq.heapify(arr)
        
        while len(arr)>k:
            heapq.heappop(arr)
        
        # for k,v in my_dict.items():
            # heapq.heappush(arr,(v,k))
            # if len(arr)>k:
            #     heapq.heappop(arr)
            # print(arr[0],arr)
        ans = []
        for tup in arr:
            ans.append(tup[1])
        return ans
