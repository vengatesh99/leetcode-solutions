class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count_map = Counter(tasks)
        lastIndex_map = {}
        lastIndex_map = defaultdict(lambda:-n-1,lastIndex_map)
        ans = 0
        string = ""
        while len(count_map.keys())>0:
            keys = count_map.keys()
            keys = sorted(keys, key = lambda x:count_map[x],reverse = True)
            isUpdate = False
            for key in keys:
                if ans-lastIndex_map[key] >n:
                    lastIndex_map[key] = ans
                    count_map[key]-=1
                    string+=key
                    ans+=1
                    if count_map[key] == 0:
                        del count_map[key]
                        del lastIndex_map[key]
                    isUpdate = True
                    break
            if not isUpdate:
                string+=" "
                ans+=1
        print(string)
        return len(string)
            
        