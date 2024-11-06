import java.util.*;

class Solution {
    public int solution(String s) {
        int answer = 0;
        
        if (s.length() % 2 == 1) {
            return 0;
        }
        
        for (int i=0; i<s.length(); i++) {
            Stack<Character> stack = new Stack<>();
            String subString = s.substring(i, s.length()) + s.substring(0, i);
            
            for (int j=0; j<subString.length(); j++) {
                char c = subString.charAt(j);
            
                if (stack.isEmpty()) {
                    stack.push(c);
                } else if (c == ')' && stack.peek() == '(') {
                    stack.pop();
                } else if (c == ']' && stack.peek() == '[') {
                    stack.pop();
                } else if (c == '}' && stack.peek() == '{') {
                    stack.pop();
                } else {
                    stack.push(c);
                }
            }
        
            if (stack.isEmpty()) {
                answer += 1;
            }
        }
        
        
        return answer;
    }
}