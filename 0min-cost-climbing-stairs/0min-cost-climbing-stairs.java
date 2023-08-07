class Solution {
    HashMap<Integer,Integer>map = new HashMap<>();
    public int minCostClimbingStairs(int[] cost) {
        return Math.min(dp(cost,0),dp(cost,1));
    }
    int dp(int[] cost, int i){
        if(i>=cost.length)return 0;
        if(map.containsKey(i))return map.get(i);
        map.put(i,Math.min(dp(cost,i+1),dp(cost,i+2))+cost[i]);
        return map.get(i);
    }
}