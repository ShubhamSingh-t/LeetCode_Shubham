class Solution {
    public void reverseString(char[] s) {
        int n = s.length;
        int start = 0;
        int e = n-1;
        char temp = 'a';
        while(start<e){
            temp = s[start];
            s[start]=s[e];
            s[e]=temp;
            start++;
            e--;
        }
        
    }
}