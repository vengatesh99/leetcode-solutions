class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hashmap = {A[i]:i for i in range(len(A))}
        C = [0]*len(A)
        for i in range(len(A)):
            j = i
            ct = 0
            while j>=0:
                if i>=hashmap[B[j]]:
                    ct+=1
                j-=1
            C[i] = ct
        return C