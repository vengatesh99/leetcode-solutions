class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]*len(s)
        if s[0]!='0':
            dp[0] = 1
        for i in range(1,len(s)):
            count = 0
            if s[i]!='0':
                count = dp[i-1]
            if s[i-1]!='0' and int(s[i-1:i+1])<=26:
                if i>1:
                    dp[i] = count+dp[i-2]
                else:
                    dp[i] = count+1
            else:
                dp[i] = count
        return dp[-1]
            
