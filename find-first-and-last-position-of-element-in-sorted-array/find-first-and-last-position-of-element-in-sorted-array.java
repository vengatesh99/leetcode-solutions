class Solution {
    public int[] searchRange(int[] nums, int target) {
        int left = 0, right = nums.length - 1;
        int[] ans = new int[2];
        ans[0] = -1;
        ans[1] = -1;
        if(nums.length == 1){
            if(target == nums[0]){
                ans[0] = 0;
                ans[1] = 0;
            }
            return ans;
        }
        while(left <= right){
            int mid = left + (right - left)/2;
            if(nums[mid]<target){
                left = mid + 1;
            }
            else if(nums[mid] > target){
                right = mid - 1;
            }
            else {
                int start = mid;
                int end = mid;
                while(start >= 0 && nums[start] == target){
                    start--;
                }
                while(end < nums.length && nums[end] == target){
                    end++;
                }
                //if(start<0)start = 0;
                //if(end == nums.length) end--;
                ans[0] = start + 1;
                ans[1] = end - 1;
                return ans;
            }
        }
        return ans;
    }
}