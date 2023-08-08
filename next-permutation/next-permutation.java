class Solution {
    public void nextPermutation(int[] nums) {
        int i = nums.length-2;
        while(i>=0&&nums[i]>=nums[i+1]){
            i--;
        }
        int j = nums.length-1;
        if(i>=0){
            while(j>i&&nums[j]<=nums[i]){
                j--;
            }
            swap(i,j,nums);
        }
        reverse(i+1,nums.length-1,nums);
    }
    void reverse(int st,int end, int[] nums){
        while(st<end){
            swap(st,end,nums);
            st++;
            end--;
        }
    }

    void swap(int i, int j, int[] nums){
        int temp = nums[i];
        nums[i] = nums[j];
        nums[j] = temp;
    }
}