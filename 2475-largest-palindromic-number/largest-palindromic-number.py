from collections import Counter
class Solution:
    def largestPalindromic(self, num: str) -> str:
        # count_map = defaultdict(int)
        odd_map = defaultdict(int)
        even_map = defaultdict(int)
        string1,string2,middle = '','',''

        count_map = Counter(num)
        sorted_list = sorted(count_map.keys(),reverse=True)
        for key in sorted_list:
            count = count_map[key]
            while count>1:
                string1+=key
                count_map[key]-=2
                count-=2
            if count == 1:
                if not middle:
                    middle = key
                    count-=1
            # if count == 0:
            #     del count_map[key]
            

        # for key,val in count_map.items():
        #     key = int(key)
        #     if val%2==0:
        #         even_map[key] = val
        #     else:
        #         odd_map[key] = val

        # even_sorted_list = sorted(even_map.keys(), reverse=True)
        # odd_sorted_list = sorted(odd_map.keys(), reverse=True)

        # if even_sorted_list:
        #     for key in even_sorted_list:
        #         if key == 0 and string1=='':
        #             break
        #         count = even_map[key]//2
        #         while count:
        #             string1 += str(key)
        #             count-=1
        
        # if odd_sorted_list:
        #     for key in odd_sorted_list:
        #         # if odd_map[key] == 1:
        #         middle = str(key)
        #         break
        i = 0

        while i<len(string1):
            if string1[i] != '0':
                break
            else:
                i+=1

        firstHalf = string1[i:]
        secondHalf = firstHalf[::-1]
        ans = firstHalf+middle+secondHalf

        return ans if len(ans)!=0 else sorted_list[0]



        