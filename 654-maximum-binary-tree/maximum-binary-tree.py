# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        n = len(nums)
        def findMax(left,right):
            maxNum,maxInd = 0,0
            for i in range(left,right+1):
                if maxNum<nums[i]:
                    maxNum = nums[i]
                    maxInd = i
            return maxNum,maxInd
        def buildTree(left,right):
            if left>right or right>=n:
                return None
            if left==right:
                return TreeNode(nums[left])
            num,index = findMax(left,right)
            print(num,index)
            node = TreeNode(num)
            node.left = buildTree(left,index-1)
            node.right = buildTree(index+1,right)
            return node
        return buildTree(0,n-1)