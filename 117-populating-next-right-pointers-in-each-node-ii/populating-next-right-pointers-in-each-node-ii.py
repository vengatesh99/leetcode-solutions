"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        queue = deque()
        if root.left:
            queue.append((root.left,1))
        if root.right:
            queue.append((root.right,1))
        prevLevel = 0
        prevNode = root
        while queue:
            node,level = queue.popleft()
            if prevLevel == level:
                prevNode.next = node  
            else:
                prevNode.next = None
            prevNode = node
            prevLevel = level
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        return root