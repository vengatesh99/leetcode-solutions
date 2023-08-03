class Solution {
    public String licenseKeyFormatting(String s, int k) {
        String ans ="";
        s = s.replaceAll("-","");
        int groups = 0;
        if(s.length()%k==0){
            groups = s.length()/k;
        }
        else groups = s.length()/k +1;
        int sz = k;
        for(int i = s.length()-1;i>=0;i--){
            if(sz==0){
                sz = k;
                ans = "-"+ans;
            }
            char ch = s.charAt(i);
            if(Character.isLetter(ch))ch = Character.toUpperCase(ch);
            ans = ch + ans;
            sz--;
        }
        return ans;
    }
}