class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        map = Counter(nums)
        ans = []
        for k,v in map.items():
            if v == 2:
                ans.append(k)
        return ans