class Solution {
    public int[] plusOne(int[] digits) {
        int[] res = new int[digits.length+1];
        int carry = 1;
        for(int i=digits.length-1;i>=0;i--){
            int sum = digits[i]+carry;
            if(sum>9){
                res[i+1] = sum%10;
                carry = sum/10;
            }
            else{
                res[i+1] = sum;
                carry = 0;
            }
        }
        if(carry==1){
            res[0] = carry;
            return res;
        }
        return Arrays.copyOfRange(res,1,res.length);
    }
}