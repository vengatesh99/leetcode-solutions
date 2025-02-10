class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        rem = needs.copy()
        memo = {}
        def checkValid(target,arr):
            for k in range(len(arr)):
                if arr[k]<target[k]:
                    return False
            return True

        def dp(rem):
            if tuple(rem) in memo:
                return memo[tuple(rem)]
            mincost = float("inf")
            for offer in special:
                if checkValid(offer,rem):
                    left = [item-offer[i] for i,item in enumerate(rem)]
                    mincost = min(mincost,offer[-1]+dp(left))
            cost = sum([rem[i]*price[i] for i in range(len(rem))])
            mincost = min(mincost,cost)
            memo[tuple(rem)] = mincost
            return mincost
        return dp(rem)
