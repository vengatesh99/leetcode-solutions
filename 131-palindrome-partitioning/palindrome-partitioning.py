class Solution:
    def partition(self, s: str) -> List[List[str]]:
        #Step 1: Break at each index, check if palin, iterate deep
        #If not palin, move to the next index, and check, and so on....
        res = []
        ans = []
        def isPalin(left,right):
            while left<right and s[left] == s[right]:
                left+=1
                right-=1
            return left >= right
        def breakString(start,end):
            if start == end:
                res.append(ans.copy())
                return
            for i in range(start,end):
                if isPalin(start,i):
                    # print(s[start:i+1])
                    ans.append(s[start:i+1])
                    breakString(i+1,end)
                    ans.pop()
        breakString(0,len(s))
        return res
                
                