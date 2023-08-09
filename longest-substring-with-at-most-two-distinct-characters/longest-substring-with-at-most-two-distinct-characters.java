class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        HashMap<Character,Integer> map = new HashMap<>();
        int l = 0, r = 0;
        int len = 0;
        while(r < s.length()){
            char ch = s.charAt(r);
            map.put(ch,map.getOrDefault(ch,0)+1);
            while(map.size() > 2){
                char left = s.charAt(l);
                map.put(left,map.get(left)-1);
                if(map.get(left) == 0)map.remove(left);
                l++;
            }
            len = Math.max(r-l+1,len);
            r++;
        }
        return len;
        
    }
}