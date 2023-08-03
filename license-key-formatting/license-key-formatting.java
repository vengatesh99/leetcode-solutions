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
        StringBuilder sb = new StringBuilder();
        for(int i = s.length()-1;i>=0;i--){
            if(sz==0){
                sz = k;
                sb = sb.append("-");
            }
            char ch = s.charAt(i);
            if(Character.isLetter(ch))ch = Character.toUpperCase(ch);
            sb = sb.append(ch);
            sz--;
        }
        return sb.reverse().toString();
    }
}