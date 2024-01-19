# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(inorder,st,end):
            nonlocal ind
            if ind >= len(preorder) or st<0 or st>end or end>=len(inorder):
                return None
            node = TreeNode(preorder[ind])
            # print(node.val)
            pos = inorder.index(preorder[ind])
            # print(ind,pos)
            ind+=1
            
            node.left = helper(inorder,st,pos-1)
            node.right = helper(inorder,pos+1,end)
            return node
        ind = 0
        root = helper(inorder,0,len(inorder)-1)
        return root