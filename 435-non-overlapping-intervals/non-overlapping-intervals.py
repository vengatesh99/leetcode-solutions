class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x:(x[1],x[0]))
        nonOverlap = 1
        curr = intervals[0]
        print(intervals)
        for i in range(1,len(intervals)):
            interval = intervals[i]
            if interval[0] < curr[1]:
                continue
            else:
                curr = interval
                nonOverlap+=1
        return len(intervals)-nonOverlap
            