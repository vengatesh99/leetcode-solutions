class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m,n = len(mat),len(mat[0])
        dist = [[float("inf") if mat[i][j] == 1 else 0 for j in range(n)] for i in range(m)]
        q = []
        visit = set()
        def bfs():
            d = 0
            while q:
                sz = len(q)
                while sz:
                    nr,nc = q.pop(0)
                    if mat[nr][nc] == 1:
                        dist[nr][nc] = min(dist[nr][nc],d)
                    for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                        x,y = nr+dr,nc+dc
                        if min(x,y)<0 or x>=m or y>=n:
                            continue
                        if (x,y) not in visit:
                            visit.add((x,y))
                            q.append((x,y))
                    sz-=1
                d+=1
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    q.append((i,j))
                    visit.add((i,j))
        bfs()
        return dist