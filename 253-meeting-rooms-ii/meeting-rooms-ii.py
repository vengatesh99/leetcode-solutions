class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        maxTime = max(v for _,v in intervals)
        minTime = min(v for v,_ in intervals)
        count = [0]*(maxTime+1)
        rooms = 0
        for s,f in intervals:
            count[s]+=1
            count[f]-=1
        for i in range(max(minTime,1),maxTime+1):
            count[i] += count[i-1]
            rooms = max(rooms,count[i])
        return rooms