class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
    def insert(self,word):
        node = self.root
        for w in word:
            if w not in node.children:
                node.children[w] = (TrieNode(),1)
            else:
                node.children[w] = (node.children[w][0],node.children[w][1]+1)
            node,_ = node.children[w]
        node.end = True
    def isPrefix(self,pre):
        node = self.root
        ans = float("inf")
        for p in pre:
            if p not in node.children:
                return 0
            node,count = node.children[p]
            ans = min(ans,count)
        return ans
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        trie = Trie()
        for word in words:
            trie.insert(word)
        ans = trie.isPrefix(pref)
        return 0 if ans == float("inf") else ans
        
        
        