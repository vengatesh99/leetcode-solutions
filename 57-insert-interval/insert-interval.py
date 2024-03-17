class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        i = 1
        intervals.append(newInterval)
        intervals.sort(key= lambda x:(x[0],x[1]))
        ans.append(intervals[0])
        while i < len(intervals):
            if intervals[i][0]<=ans[-1][1]:
                ans[-1][1] = max(intervals[i][1],ans[-1][1])
            else:
                ans.append(intervals[i])
            i+=1
        return ans