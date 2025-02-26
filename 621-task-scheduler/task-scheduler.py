from collections import Counter
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        pq = [(-v,ord(k)-ord("A")) for k,v in counter.items()]
        heapq.heapify(pq)
        count = 0
        while pq:
            cycles = n+1
            temp_arr = {}
            while cycles>0 and pq:
                top,ind = heapq.heappop(pq)
                top = -top-1
                if top:
                    temp_arr[ind] = top
                count+=1
                cycles-=1
            if cycles>0 and temp_arr:
                count+=cycles
            for i,f in temp_arr.items():
                heapq.heappush(pq,(-f,i))
        return count