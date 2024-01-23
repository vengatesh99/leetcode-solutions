class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x:(x[0],x[1]))
        # nonOverlap = set()
        # nonOverlap.add((points[i][0],points[i][1]))
        nonOverlap = 1
        st = points[0][0]
        end = points[0][1]
        for i in range(1,len(points)):
            interval = points[i]
            if interval[0]<=end:
                st = interval[0]
                end = min(interval[1],end)
            else:
                nonOverlap+=1
                st,end = interval[0],interval[1]
        return nonOverlap
            