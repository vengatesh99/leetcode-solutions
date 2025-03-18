class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, composition: List[List[int]], stock: List[int], cost: List[int]) -> int:
        alloys = 0
        def isFeasible(arr,target):
            s = 0
            for i,c in enumerate(cost):
                units = max(0,(arr[i]*target-stock[i]))
                s+=units*c
            return s<=budget
            
        for i in range(len(composition)):
            s1,s2 = 0,0
            for s,c in zip(stock,cost):
                s1+=s*c
            for m,c in zip(composition[i],cost):
                s2+=m*c
            r = (s1+budget)//s2
            # r = 10**9
            l = 0
            while l<=r:
                mid = (l+r)//2
                if isFeasible(composition[i],mid):
                    l = mid+1
                else:
                    r = mid-1
            alloys = max(alloys,l-1)
        return alloys
             