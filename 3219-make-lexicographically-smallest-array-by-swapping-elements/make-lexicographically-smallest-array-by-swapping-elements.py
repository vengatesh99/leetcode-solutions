class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        groupMapping = {}
        for num in sorted(nums):
            if not groups or abs(groups[-1][-1]-num)>limit:
                groups.append(deque())
            groups[-1].append(num)
            groupMapping[num] = len(groups)-1
        ans = [-1]*len(nums)
        for i,num in enumerate(nums):
            index = groupMapping[num]
            ans[i] = groups[index].popleft()
        return ans
        
