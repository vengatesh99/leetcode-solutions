class Solution:
    def minSwaps(self, data: List[int]) -> int:
        n = len(data)
        ones = 0
        for i in range(n):
            if data[i] == 1:
                ones+=1
        i,j = 0,0
        maxOnes,newOnes = 0,0
        while j<n:
            if j-i+1 > ones:
                if data[i] == 1 and newOnes!=0:
                    newOnes-=1
                i+=1
                maxOnes = max(maxOnes,newOnes)
            else:
                if data[j] == 1:
                    newOnes+=1
                if j-i+1 == ones:
                    maxOnes = max(maxOnes,newOnes)
                j+=1

        maxOnes = max(newOnes,maxOnes)
        print(ones,maxOnes)
        return ones-maxOnes