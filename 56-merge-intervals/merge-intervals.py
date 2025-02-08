class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sorted_intervals = sorted(intervals, key = lambda x: x[0])
        intervals.sort()
        # merged = [sorted_intervals[0]]
        # merged[0] = sorted_intervals[0]
        i = 1
        n = len(intervals)
        k = 0
        while i<n:
            if intervals[i][0]<=intervals[k][1]:
                intervals[k][1] = max(intervals[k][1],intervals[i][1])
            else:
                k+=1
                intervals[k] = intervals[i]
            i+=1
        return intervals[:k+1]
