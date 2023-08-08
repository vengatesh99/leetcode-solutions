class Solution {
    public int totalFruit(int[] fruits) {
        int st = 0, end = 0;
        int ans = -1;
        HashMap<Integer,Integer>map = new HashMap<>();
        while(end<fruits.length){
            map.put(fruits[end],map.getOrDefault(fruits[end],0)+1);
            while(map.size()>2){
                map.put(fruits[st],map.get(fruits[st])-1);
                if(map.get(fruits[st])==0)map.remove(fruits[st]);
                st++;
            }
            ans = Math.max(ans,end-st+1);
            end++;
        }
        return ans;
    }
}