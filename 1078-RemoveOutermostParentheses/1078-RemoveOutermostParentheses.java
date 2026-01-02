// Last updated: 1/2/2026, 12:17:45 PM
class Solution {
    public String removeOuterParentheses(String s) {
       String str = s;
    StringBuilder ans = new StringBuilder();
    int iterator= 0;
    int count =0;
            while (iterator < str.length()) {
                if ( str.charAt(iterator) == '(') {
                    count++;
                }
                if (count>1){
                    ans.append(str.charAt(iterator));
                }
                if ( str.charAt(iterator) == ')') {
                    count--;
                }
                iterator++;
            }
            return ans.toString();
    }
    }
