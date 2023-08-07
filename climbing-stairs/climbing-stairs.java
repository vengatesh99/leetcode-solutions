class Solution {
    HashMap<Integer,Integer>map = new HashMap<>();
    public int climbStairs(int n) {
        return climb(n,0);
    }
    int climb(int n, int i){
        if(i==n)return 1;
        if(i>n)return 0;
        if(map.containsKey(i))return map.get(i);
        int sum = climb(n,i+1)+climb(n,i+2);
        map.put(i,sum);
        return map.get(i);
    }
}