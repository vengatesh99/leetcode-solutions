class Solution {
    public int maxDistToClosest(int[] seats) {
        int[] left = new int[seats.length];
        int[] right = new int[seats.length];
        int max = -2;
        left[0] = seats[0]==1?0:Integer.MAX_VALUE;
        right[seats.length-1] = seats[seats.length-1] == 1?seats.length-1:Integer.MAX_VALUE;
        for(int i=1;i<seats.length;i++){
            if(seats[i]==1)left[i] = i;
            else{
                left[i] = left[i-1];
            }
        }
        for(int i=seats.length-2;i>=0;i--){
            right[i] = seats[i]==1?i:right[i+1];
        }
        for(int i=0;i<seats.length;i++){
            if(seats[i]==0){
                if(i==0){
                    max = Math.max(right[0],max);
                }
                else if(i==seats.length-1) max = Math.max(max,i-left[i]);
                else max = Math.max(Math.min(i-left[i],right[i]-i),max);
            }
        }
        return max;
    }
}