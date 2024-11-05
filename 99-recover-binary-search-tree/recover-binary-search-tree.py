# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        def swapNodes(root):
            nonlocal swap1,swap2,pred
            if not root:
                return
            swapNodes(root.left)
            if pred:
                if pred.val>root.val:
                    swap2 = root
                    if not swap1:
                        swap1 = pred
                    else:
                        return
            pred = root
            swapNodes(root.right)
    
        swap1 = swap2 = pred = None
        swapNodes(root)
        swap1.val,swap2.val = swap2.val,swap1.val

        