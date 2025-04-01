class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = "".join(sorted(s1))
        s2 = "".join(sorted(s2))
        n = len(s1)
        i,j = 0,0
        while i<n and s1[i]<=s2[j]:
            i+=1
            j+=1
        if i == n:
            return True
        i,j = 0,0
        while i<n and s1[i]>=s2[j]:
            i+=1
            j+=1
        if i == n:
            return True
        return False