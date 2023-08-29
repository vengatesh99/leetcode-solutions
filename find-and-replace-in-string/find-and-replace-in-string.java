class Solution {
    public String findReplaceString(String s, int[] indices, String[] sources, String[] targets) {
        StringBuilder sb = new StringBuilder(s);
        StringBuilder ans = new StringBuilder();
        int k=0;
        HashMap<Integer,String>map1 = new HashMap<>();
        HashMap<Integer,String>map2 = new HashMap<>();
        for(int i=0;i<indices.length;i++){
            int len = sources[i].length();
            if(indices[i]+len>s.length())continue;
            if(s.substring(indices[i],indices[i]+len).equals(sources[i])){
                map1.put(indices[i],sources[i]);
                map2.put(indices[i],targets[i]);
            }
        }
        int i=0;
        while(i<s.length()){
            if(map1.containsKey(i)&&
              s.startsWith(map1.get(i),i)){
                ans.append(map2.get(i));
                    i+=map1.get(i).length();
            }
            else {
                ans.append(s.charAt(i));
                i++;
            }
        }
        return ans.toString();
    }
}