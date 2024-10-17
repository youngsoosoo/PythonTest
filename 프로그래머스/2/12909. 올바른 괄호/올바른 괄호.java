import java.util.*;

class Solution {
    boolean solution(String s) {
        boolean answer = true;

        Stack<Character> stack = new Stack<>();
        
        for (int i=0; i<s.length(); i++) {
            char c = s.charAt(i);
            if (!stack.isEmpty() && stack.peek() != c && c == ')') {
                stack.pop();
            } else {
                stack.push(c);
            }
        }
        
        if (!stack.isEmpty()) {
            answer = false;
        }
        
        return answer;
    }
}