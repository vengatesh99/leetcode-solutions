# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    leftB = []
    rightB = []
    leaves = []
    def addLeftBoundary(self,node):
        if not node:
            return
        if not node.left and not node.right:
            return
        self.leftB.append(node.val)
        if node.left:
            self.addLeftBoundary(node.left)
        else:
            self.addLeftBoundary(node.right)
        
    def addRightBoundary(self,node):
        
        if not node:
            return
        if not node.left and not node.right:
            return
        print(node.val)
        if node.right:
            self.addRightBoundary(node.right)
        else:
            self.addRightBoundary(node.left)
        self.rightB.append(node.val)
        

    def addLeaves(self,node):
        if node is None:
            return
        if node.left is None and node.right is None:
            self.leaves.append(node.val)
            return
        self.addLeaves(node.left)
        self.addLeaves(node.right)

    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        self.leftB = []
        self.rightB = []
        self.leaves = []
        if root.left == None and root.right == None:
            return [root.val]
        self.addLeftBoundary(root.left)
        self.addRightBoundary(root.right)
        self.addLeaves(root)
        print(self.leaves)
        ans = [root.val]+self.leftB+self.leaves+self.rightB

        return ans