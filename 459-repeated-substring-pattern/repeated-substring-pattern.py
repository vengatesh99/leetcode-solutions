class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i = 0
        temp_substring = ""
        n = len(s)
        while i < len(s)-1:
            temp_substring += s[i]
            # k = len(temp_substring)
            check_string = ""
            if n%(i+1) == 0:
                count = n//(i+1)
                while count > 0:
                    check_string+=temp_substring
                    count-=1
                if check_string == s:
                    return True
            i+=1
        return False