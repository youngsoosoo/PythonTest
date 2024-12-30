import java.util.*;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        
        Stack<Integer> stack = new Stack<>();
        // 커서 역할
        int idx = 0;
            
        for (int i=1; i<=order.length; i++) {
            
            if(order[idx] != i) {
                stack.push(i);
            } else {
                idx++;
                answer++;
            }
            while(!stack.isEmpty() && stack.peek() == order[idx]) {
                stack.pop();
                idx++;
                answer++;
            }
        }
        
        return answer;
    }
}