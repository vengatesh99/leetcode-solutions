class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n+1):
            ct = 0
            while i !=0:
                if i & 1 == 1:
                    ct+=1
                i = i>>1
            ans.append(ct)
        return ans