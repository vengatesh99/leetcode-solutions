"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return None
        def helper(root):
            nonlocal pred,succ
            if not root:
                return None
            
            helper(root.left)
            if not pred:
                pred = root
                if not succ:
                    succ = pred
            else:
                pred.right = root
                root.left = pred
                pred = root
            right = helper(root.right)
        
        
        pred,succ = None,None
        helper(root)
        pred,succ = succ,pred
        pred.left = succ
        succ.right = pred
        return pred