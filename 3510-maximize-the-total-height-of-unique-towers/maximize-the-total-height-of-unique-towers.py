class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        maximumHeight.sort(reverse=True)
        n = len(maximumHeight)
        s = maximumHeight[0]
        # visit = set()
        # visit.add(maximumHeight[0])
        for i in range(n-1):
            if maximumHeight[i]<=maximumHeight[i+1]:
                maximumHeight[i+1] = maximumHeight[i]-1
            if maximumHeight[i+1] == 0:
                return -1
            # s+=maximumHeight[i]
            # visit.add(maximumHeight[i])
        return sum(maximumHeight)