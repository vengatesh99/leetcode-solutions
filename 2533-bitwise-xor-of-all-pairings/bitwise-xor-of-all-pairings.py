class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        n,m = len(nums1),len(nums2)
        res = 0
        for num in nums1:
            if m%2!=0:
                res^=num
        for num in nums2:
            if n%2!=0:
                res^=num
        return res