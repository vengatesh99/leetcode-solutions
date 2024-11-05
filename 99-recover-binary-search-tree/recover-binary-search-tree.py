# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.inorder = []
    def recoverUtil(self,root,inorder):
        if not root:
            return
        self.recoverUtil(root.left,inorder)
        inorder.append(root.val)
        self.recoverUtil(root.right,inorder)

    def traverse(self,root,swap1,swap2):
        if not root:
            return
        self.traverse(root.left,swap1,swap2)
        if root.val == swap1:
            root.val = swap2
        elif root.val == swap2:
            root.val = swap1
            return
        self.traverse(root.right,swap1,swap2)
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        sol = Solution()
        inorder = sol.inorder
        self.recoverUtil(root,inorder)
        print(inorder)
        swap = 0
        swap1,swap2 = -1,-1
        for i in range(1,len(inorder)):
            if inorder[i-1]>inorder[i]:
                if swap>0:
                    swap2 = i
                    break
                swap1 = i-1
                swap+=1
        if swap2 == -1:
            swap2 = swap1+1
        self.traverse(root,inorder[swap1],inorder[swap2])
        
            
        