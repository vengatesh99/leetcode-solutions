class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # hashmap = {A[i]:i for i in range(len(A))}
        hashset = set()
        C = [0]*len(A)
        for i in range(len(A)):
            # j = i
            # ct = 0
            # while j>=0:
            #     if i>=hashmap[B[j]]:
            #         ct+=1
            #     j-=1
            ct = 0
            if B[i] in hashset:
                ct+=1
            hashset.add(B[i])
            if A[i] in hashset:
                ct+=1
            hashset.add(A[i])
            C[i] = C[i-1] + ct
            # C[i] = ct
        return C