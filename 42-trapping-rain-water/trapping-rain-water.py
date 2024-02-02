class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_max = [-1]*len(height)
        right_max = [-1]*len(height)
        maxL = -1
        maxR = -1
        ans = 0
        for i in range(1,len(height)):
            left_max[i] = max(left_max[i-1],height[i-1])
        for i in range(len(height)-2,-1,-1):
            right_max[i] = max(right_max[i+1],height[i+1])
        for i in range(len(height)):
            if left_max[i] == -1 or right_max[i] == -1:
                continue
            if height[i]>min(left_max[i],right_max[i]):
                continue
            ans+=min(left_max[i],right_max[i])-height[i]
        return ans