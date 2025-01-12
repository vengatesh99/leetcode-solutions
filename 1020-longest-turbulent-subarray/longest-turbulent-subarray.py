class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        left,right = 0,0
        n = len(arr)
        prevSign = -1
        ans = 1
        while right < n-1:
            if left == right:
                right+=1
                continue
            if left+1 == right:
                if arr[left]>arr[right]:
                    prevSign = 1
                elif arr[left]<arr[right]:
                    prevSign = 0
                else:
                    left = right
                    continue
            if prevSign:
                if arr[right]<arr[right+1]:
                    right+=1
                    prevSign = 0
                else:
                    ans = max(ans,right-left+1)
                    left = right
            else:
                if arr[right]>arr[right+1]:
                    right+=1
                    prevSign = 1
                else:
                    ans = max(ans,right-left+1)
                    left = right
        if prevSign!=-1:
            ans = max(ans,right-left+1)
        else:
            if left+1 == right and arr[left]!=arr[right]:
                ans = 2
        return ans
            



