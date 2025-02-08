class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key = lambda x: x[0])
        merged = [sorted_intervals[0]]
        merged[0] = sorted_intervals[0]
        i = 1
        while i<len(intervals):
            while i<len(sorted_intervals) and sorted_intervals[i][0]<=merged[-1][1]:
                print(i)
                merged[-1][1] = max(sorted_intervals[i][1],merged[-1][1])
                i+=1
            if i == len(intervals):
                break
            merged.append(sorted_intervals[i])
            i+=1
        return merged
