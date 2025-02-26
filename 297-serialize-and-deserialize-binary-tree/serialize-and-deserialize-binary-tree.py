# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def __init__(self):
        self.serialized  = []
        self.i = 0
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def dfs(node):
            if not node:
                self.serialized.append('N')
                return
            self.serialized.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(self.serialized)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data_list = data.split(",")
        def construct():
            if self.i >= len(data_list):
                return None
            if data_list[self.i] == 'N':
                self.i+=1
                return None
            node = TreeNode(int(data_list[self.i]))
            self.i+=1
            node.left = construct()
            node.right = construct()
            return node
        root = construct()
        return root
        
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))