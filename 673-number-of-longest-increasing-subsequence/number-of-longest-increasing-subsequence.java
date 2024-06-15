class Solution {
    public int findNumberOfLIS(int[] nums) {
        int n = nums.length;
        int maxlen = 0;
        int[] lis = new int[n];
        int[] count = new int[n];
        int ans = 0;
        Arrays.fill(lis,1);
        Arrays.fill(count,1);

        for(int i=1;i<n;i++){
            for(int j=i-1;j>=0;j--){
                if(nums[i]>nums[j]){
                    if(lis[j]+1 > lis[i]){
                        count[i] = 0;
                        lis[i] = lis[j]+1;
                    }
                    if(lis[j]+1 == lis[i]){
                        count[i] +=count[j];
                    }
                }
            }
        }
        for(int len:lis){
            maxlen = Math.max(maxlen,len);
        }
        for(int a:count){
            System.out.print(a+" ");
        }
        for(int i=0;i<n;i++){
            if(maxlen == lis[i]){
                ans+=count[i];
            }
        }
        return ans;
    }
}