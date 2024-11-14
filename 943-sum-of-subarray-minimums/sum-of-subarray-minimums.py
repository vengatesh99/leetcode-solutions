class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = []
        stack.append(0)
        ans = 0
        n = len(arr)
        for i in range(len(arr)):
            if arr[i]>=arr[stack[-1]]:
                stack.append(i)
            else:
                while stack and arr[i]<arr[stack[-1]]:
                    idx = stack.pop()
                    prev_idx = stack[-1] if stack else -1
                    ans+=arr[idx]*(idx-prev_idx)*(i-idx)
                stack.append(i)
        while stack:
            idx = stack.pop()
            prev_idx = stack[-1] if stack else -1
            ans+= arr[idx]*(n-idx)*(idx-prev_idx)
        return ans%(1000000007)
                



