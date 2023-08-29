class Solution {
    public boolean backspaceCompare(String s, String t) {
        Stack<Character>st = new Stack<>();
        Stack<Character>st2 = new Stack<>();
        for(char ch:s.toCharArray()){
            if(ch!='#')st.push(ch);
            else if(!st.isEmpty())st.pop();
        }
        for(char ch:t.toCharArray()){
            if(ch!='#')st2.push(ch);
            else if(!st2.isEmpty())st2.pop();
        }
        if(st.size()!=st2.size())return false;
        while(!st.isEmpty()&&!st2.isEmpty()){
            char ch1 = st.pop();
            char ch2 = st2.pop();
            if(ch1!=ch2)return false;
        }
        return st.size()==st2.size();
    }
}