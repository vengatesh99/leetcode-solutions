# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        in_map = {}
        for i,node in enumerate(inorder):
            in_map[node] = i
        idx = len(postorder)-1
        def construct(l,r):
            nonlocal idx
            if idx < 0:
                return None
            if l>r:
                return None
            root_ind = in_map[postorder[idx]]
            if root_ind>r or root_ind<l:
                return None
            root = TreeNode(postorder[idx])
            idx-=1
            root.right = construct(root_ind+1,r)
            root.left = construct(l,root_ind-1)
            return root
        return construct(0,len(postorder)-1)