class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i,j = 0,0
        while i<len(firstList) and j<len(secondList):
            if firstList[i][0]>=secondList[j][0]:
                firstList.insert(i,secondList[j])
                j+=1
            i+=1
        while j<len(secondList):
            firstList.append(secondList[j])
            j+=1
        print(firstList)
        i = 1
        result = []
        while i<len(firstList):
            j = i-1
            if i<len(firstList) and firstList[j][1]>=firstList[i][0]:
                while i<len(firstList) and firstList[j][1]>=firstList[i][0]:
                    result.append([firstList[i][0],min(firstList[i][1],firstList[j][1])])
                    i+=1
            else:
                i+=1
        return result

            