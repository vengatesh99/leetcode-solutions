from collections import Counter
class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        #store words1 in hashmap
        #traverse each word in words2, check if the frequencey of each character is less than
        #/equal to every hashmap
        #efficient way to match a string?
        ans = []
        word_freq = defaultdict(int)
        for word in words2:
            map = defaultdict(int)
            for ch in word:
                map[ch]+=1
            for k,v in map.items():
                word_freq[k] = max(word_freq[k],v)
        print(word_freq)
        for word in words1:
            mydict = Counter(word)
            add = False
            count = 0
            for k,v in mydict.items():
                if k in word_freq and v>=word_freq[k]:
                    count+=1
            if count == len(word_freq):
                ans.append(word)

        return ans

                

            
            