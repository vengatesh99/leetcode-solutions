class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        prefixSum = [0]*(n+1)
        for L,R,direction in shifts:
            prefixSum[L]+= -1 if direction else 1
            prefixSum[R+1]+= 1 if direction  else -1
        arr = [ord(c)-ord('a') for c in s]
        d = 0
        for i in reversed(range(len(prefixSum))):
            d+=prefixSum[i]
            arr[i-1]=(d+arr[i-1])%26
        s = [chr(ord("a")+c) for c in arr]
        return "".join(s)

            