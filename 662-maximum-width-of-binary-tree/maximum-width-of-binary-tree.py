# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        queue.append((root,0))
        queue.append((None,-1))
        ans = 0
        left = 0
        while queue:
            node,ind = queue.popleft()
            if node == None:
                if not queue:
                    return ans
                else:
                    queue.append((None,-1))
                left = -1
            else:
                if node.left:
                    queue.append((node.left,2*ind+1))
                if node.right:
                    queue.append((node.right,2*ind+2))
            if left<0:
                left = ind
            else:
                # print(left,ind)
                ans = max(ans,ind-left+1)
                # print(ans)
        return ans