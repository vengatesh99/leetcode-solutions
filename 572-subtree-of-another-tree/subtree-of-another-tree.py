# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def serializeTree(self,root,treeList):
        if not root:
            treeList.append("#")
            return
        treeList.append("^"+str(root.val))
        self.serializeTree(root.left,treeList)
        self.serializeTree(root.right,treeList)

    def kmp(self,string,substring):
        n = len(substring)
        lps = [-1]*n
        i,j = 0,1
        
        while j<n:
            if substring[i] == substring[j]:
                lps[j] = i
                i+=1
                j+=1
            else:
                if lps[i-1] > 0:
                    i = lps[i-1]+1
                else:
                    i = 0
                    lps[j] = -1
                    j+=1
        i,j = 0,0
        while i<len(string):
            if string[i] == substring[j]:
                i+=1
                j+=1
                if j == n:
                    return True
            else:
                if j == 0:
                    i+=1
                else:
                    j = lps[j-1]+1
        return False
        
                


    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        treeList,subTreeList = [],[]
        self.serializeTree(root,treeList)
        self.serializeTree(subRoot,subTreeList)
        treeStr = "".join(treeList)
        subTreeStr = "".join(subTreeList)
        print(treeStr,subTreeStr)
        return self.kmp(treeStr,subTreeStr)