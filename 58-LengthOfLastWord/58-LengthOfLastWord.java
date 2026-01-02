// Last updated: 1/2/2026, 12:18:51 PM
class Solution {
    public int lengthOfLastWord(String s) {
        String[] str = s.split(" ");
     int n=str.length;
      int lengthoflast= str[n-1].length();
        return lengthoflast;
    }
}