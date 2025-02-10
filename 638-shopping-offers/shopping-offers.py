class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        rem = needs.copy()
        memo = {}
        def checkValid(target,arr):
            for k in range(len(arr)):
                if arr[k]<target[k]:
                    return False
            return True
        @lru_cache(None)
        def dp(rem):
            mincost = float("inf")
            remList = list(rem)
            for offer in special:
                if checkValid(offer,remList):
                    left = [item-offer[i] for i,item in enumerate(remList)]
                    mincost = min(mincost,offer[-1]+dp(tuple(left)))
            cost = sum([rem[i]*price[i] for i in range(len(remList))])
            mincost = min(mincost,cost)
            return mincost
        return dp(tuple(rem))
