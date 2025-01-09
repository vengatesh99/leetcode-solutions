class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for s,e in zip(word,reversed(word)):
            if (s,e) not in node.children:
                node.children[(s,e)] = TrieNode()
            node = node.children[(s,e)]
            node.count+=1
        
    def isPrefixAndSuffix(self,word):
        node = self.root
        for s,e in zip(word,reversed(word)):
            if (s,e) not in node.children:
                return 0
            node = node.children[(s,e)]
        return node.count



class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        ans = 0
        for word in reversed(words):
            ans+=trie.isPrefixAndSuffix(word)
            trie.insert(word)
        return ans
        