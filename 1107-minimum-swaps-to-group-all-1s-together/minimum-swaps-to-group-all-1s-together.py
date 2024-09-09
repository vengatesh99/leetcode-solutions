class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = 0
        for num in data:
            if num == 1:
                ones+=1
        onesInSubArr = 0
        maxOnes = 0
        i,j,n = 0,0,len(data)
        if ones == 0:
            return 0
        while j<n:
            while j<n and j-i+1<=ones:
                onesInSubArr += data[j]
                maxOnes = max(maxOnes,onesInSubArr)
                j+=1
            while i<j and j-i+1>ones:
                onesInSubArr -= data[i]
                i+=1

        return ones-maxOnes
            
        
        

