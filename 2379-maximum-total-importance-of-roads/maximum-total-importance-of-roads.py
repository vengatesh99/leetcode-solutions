class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degree = defaultdict(int)
        ranking = defaultdict(int)
        ans = 0
        for a,b in roads:
            degree[a]+=1
            degree[b]+=1
        for i in range(n):
            if i not in degree:
                degree[i] = 0
        sorted_list = sorted(degree, key = lambda x : degree[x])
        count = 1
        for k in sorted_list:
            ranking[k] = count
            count+=1
        for src,dest in roads:
            ans+=ranking[src]+ranking[dest]
        return ans