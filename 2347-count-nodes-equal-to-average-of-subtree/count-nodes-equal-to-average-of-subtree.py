# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.ans = 0
        def helper(root):
            if root == None:
                return 0,0
            left,n1 = helper(root.left)
            right,n2 = helper(root.right)
            if (left+right+root.val)//(n1+n2+1) == root.val:
                print(root.val)
                self.ans+=1
            return left+right+root.val,n1+n2+1
        helper(root)
        return self.ans