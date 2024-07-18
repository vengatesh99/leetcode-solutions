# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkSubTree(self,root,subRoot):
        if (root and not subRoot) or (not root and subRoot):
            return False
        if not root and not subRoot:
            return True
        return root.val == subRoot.val and self.checkSubTree(root.left,subRoot.left) and self.checkSubTree(root.right,subRoot.right)

    def isSubTreeUtil(self,root,subRoot):
        if not root:
            return False
        if root.val == subRoot.val:
            if self.checkSubTree(root,subRoot):
                return True
        return self.isSubTreeUtil(root.left,subRoot) or self.isSubTreeUtil(root.right,subRoot)


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.isSubTreeUtil(root,subRoot)