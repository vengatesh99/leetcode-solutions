# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pprint import pprint
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        graph = defaultdict(list)
        leaves = set()
        self.ans = 0
        def constructGraph(node):
            if not node:
                return None
            if node.left == None and node.right == None:
                leaves.add(node)
                return node
            
            left = constructGraph(node.left)
            right = constructGraph(node.right)
            if left:
                graph[node].append(left)
                graph[left].append(node)
            if right:
                graph[node].append(right)
                graph[right].append(node)
            return node
        
        constructGraph(root)

        def dfs(node,visited,dist):
            if node in visited or dist>distance:
                return
            visited.add(node)
            if node in leaves and  dist>0:
                self.ans+=1
                
            for neib in graph[node]:
                dfs(neib,visited,dist+1)
                
        for leaf in leaves:
            dfs(leaf,set(),0)
        # print(leaves)
        return self.ans//2