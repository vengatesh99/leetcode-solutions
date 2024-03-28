class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq_map = defaultdict(int)
        i,j,n = 0,0,len(nums)
        ans = 1
        while j<n:
            freq_map[nums[j]]+=1
            while i<j and freq_map[nums[j]]>k:
                freq_map[nums[i]]-=1
                if freq_map[i] == 0:
                    del freq_map[i]
                i+=1
            print(i,j)  
            ans = max(ans, j-i+1)
            
            j+=1
        # ans = max(ans,j-i+1)
        return ans
