class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        result = [points[0]]
        n = len(points)
        for i in range(1,n):
            if points[i][0] > result[-1][1]:
                result.append(points[i])
            else:
                result[-1][1] = min(result[-1][1],points[i][1])
        return len(result)
