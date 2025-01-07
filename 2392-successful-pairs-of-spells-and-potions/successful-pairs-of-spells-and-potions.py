class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        def feasible(potion,spell):
            return potion*spell>=success
        for spell in spells:
            left,right = 0,len(potions)-1
            while left<right:
                mid = left+(right-left)//2
                if feasible(potions[mid],spell):
                    right = mid
                else:
                    left = mid+1
            if potions[left]*spell<success:
                left+=1
            ans.append(len(potions)-left)
        return ans
            