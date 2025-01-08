class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def add(self,word):
        curr = self.root
        for w in word:
            if w not in curr.children:
                curr.children[w] = TrieNode()
            curr = curr.children[w]
        curr.end = True
    def isPrefix(self,word1):
        # if word2 not in visit:
        #     self.add(word2,visit)
        curr = self.root
        length = 0
        for w in word1:
            if curr.end:
                if w in curr.children:
                    length+=1
                break
            if w not in curr.children:
                break 
            curr = curr.children[w]
            length+=1
        return length
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1 = [str(num) for num in arr1]
        arr2 = [str(num) for num in arr2]
        trie = Trie()
        ans = 0
        for num2 in arr2:
            trie.add(num2)
        for num1 in arr1:
            # for num2 in arr2:
            ans = max(ans,trie.isPrefix(num1))
        return ans
