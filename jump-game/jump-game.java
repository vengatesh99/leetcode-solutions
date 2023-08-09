class Solution {
    HashMap<Integer,Boolean> map;
    public boolean canJump(int[] nums) {
        map = new HashMap<>();
        boolean ans = dp(0,nums);
        return ans;
    }
    boolean dp(int i, int[] nums){
        if(i>=nums.length-1){
            return true;
        }
        if(map.containsKey(i))return map.get(i);
        for(int ind = nums[i];ind>=1;ind--){
            boolean val = dp(i+ind,nums);
            if(val){
                map.put(i,true);
                return true;
            }
        }
        map.put(i,false);
        return map.get(i); 
    }
}