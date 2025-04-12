# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        path = float("-inf")
        def maxPath(node):
            nonlocal path
            if not node:
                return float("-inf")
            left = maxPath(node.left)
            right = maxPath(node.right)
            path = max(path,left,right,max(left,0)+max(right,0)+node.val)
            return max(left,right,0)+node.val
        maxPath(root)
        return path