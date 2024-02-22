dictionary = defaultdict(int)
class Solution:
    
    def is_valid(self,s1):
        if s1 == "":
            return True
        return not (s1.startswith("0") or int(s1) == 0 or int(s1)>26)
    
    def calculate(self,s,s1,start):
        global dictionary
        print(s1,s[start:])
        if not self.is_valid(s1):
            return 0
        if start>=len(s):
            return 1
        if s[start:] in dictionary:
            return dictionary[s[start:]]
        
        ans = 0
        count= 0
        for i in range(start,len(s)) :
            count += self.calculate(s,s[start:i+1],i+1)
        ans += count
        dictionary[s[start:]] = ans
        return ans
        

    def numDecodings(self, s: str) -> int:
        return self.calculate(s[:],"",0)