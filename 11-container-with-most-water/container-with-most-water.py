class Solution:
    def maxArea(self, height: List[int]) -> int:
        i,j = 0,len(height)-1
        ans = 0
        while i<j:
            ans = max(ans, min(height[i],height[j])*(j-i))
            if height[i]<height[j]:
                i+=1
            elif height[i]>height[j]:
                j-=1
            else:
                i+=1
                j-=1
        # while i<j:
        #     ans = max(ans,min(height[i],height[j])*(j-i))
        #     if min(height[i],height[j-1])>min(height[i+1],height[j]):
        #         j-=1
        #     elif min(height[i],height[j-1])<min(height[i+1],height[j]):
        #         i+=1
        #     else:
        #         i+=1
        #         j-=1
        return ans