# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if root.left == None and root.right == None:
            return [root.val]
        leftB = root.left
        rightB = root.right
        leftList = []
        rightList = []
        leavesList = []
        while leftB and (leftB.left or leftB.right):
            leftList.append(leftB.val)
            leftB = leftB.left if leftB.left else leftB.right
        while rightB and (rightB.left or rightB.right):
            rightList.append(rightB.val)
            rightB = rightB.right if rightB.right else rightB.left
        def getLeaves(tempRoot):
            if not tempRoot:
                return
            if not tempRoot.left and not tempRoot.right:
                leavesList.append(tempRoot.val)
                return
            getLeaves(tempRoot.left)
            getLeaves(tempRoot.right)
        getLeaves(root)
        return [root.val]+leftList + leavesList + rightList[::-1]