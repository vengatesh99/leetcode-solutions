class Solution:
    def findMaxSum(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        hm = {}
        
        pq = []
        rs = 0
        ans = [0 for _ in range(len(nums1))]

        arr = [(nums1[i],i) for i in range(len(nums1))]
        arr.sort(key = lambda x: x[0])
        j = 0
        for i in range(len(arr)):
            while j<i and arr[j][0]<arr[i][0]:
                rs+=nums2[arr[j][1]]
                heapq.heappush(pq,nums2[arr[j][1]])
                if len(pq) > k:
                    rs-=heapq.heappop(pq)
                j+=1
            ans[arr[i][1]] = rs
                    
        return ans
    
                