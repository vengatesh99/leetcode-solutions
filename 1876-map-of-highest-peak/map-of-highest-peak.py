class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m,n = len(isWater),len(isWater[0])
        queue = [(i, j) for i in range(m) for j in range(n) if isWater[i][j] != 0]
        ans = [[-1 for j in range(n)] for i in range(m)]
        for i,j in queue:
            ans[i][j] = 0
        maxH = -1
        print(queue)
        while queue:
            row,col = queue.pop(0)
            for r,c in [[0,1],[0,-1],[-1,0],[1,0]]:
                newR,newC = row+r,col+c
                if min(newR,newC)>=0 and newR<m and newC<n and ans[newR][newC] == -1:
                    queue.append((newR,newC))
                    ans[newR][newC] = ans[row][col]+1
                    maxH = max(maxH,ans[row][col])
        return ans
            
                