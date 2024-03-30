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
            # if min(height[i+1],height[j])<min(height[i],height[j-1]):
            #     j-=1
            # elif min(height[i+1],height[j])>min(height[i],height[j-1]):
            #     i+=1
            # else:
            #     i+=1
            #     j-=1

        return ans