class Solution {
    public List<List<Integer>> findMissingRanges(int[] nums, int lower, int upper) {
        List<List<Integer>>result = new ArrayList<>();
        if(nums.length==0){
            add(result,lower,upper);
            return result;
        }
        if(lower<nums[0]){
            add(result,lower,nums[0]-1);
        }
        for(int i=0;i<nums.length-1;i++){
            int l = nums[i]+1;
            int h = nums[i+1]-1;
            if(l<=h){
                add(result,l,h);
            }
        }
        if(nums[nums.length-1]<upper){
            add(result,nums[nums.length-1]+1,upper);
        }
        return result;
    }
    void add(List<List<Integer>>result,int l, int h){
        List<Integer>temp = new ArrayList<>();
        temp.add(l);
        temp.add(h);
        result.add(temp);
    }
}