class Solution:
    def calculateCost(self, days, day, idx, costs, memo):
        if day < 0:
            return 0
        if idx < 0:
            return 0
        if day in memo:
            return memo[day]
        if day == days[idx]:
            idx -=1
            total = min(costs[0] + self.calculateCost(days,day-1,idx,costs,memo),
                    costs[1] + self.calculateCost(days,day-7,idx,costs,memo),
                    costs[2] + self.calculateCost(days,day-30,idx,costs,memo))
        else:
            total = self.calculateCost(days,day-1,idx,costs,memo)
        memo[day] = total
        print(day,total)
        return memo[day]
    
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = defaultdict(int)
        memo[0] = 0
        return self.calculateCost(days,days[-1],len(days)-1,costs,memo)