import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        for (int i=0; i<prices.length-1; i++) {
            boolean flag = false;
            int cnt = 0;
            for (int j=i+1; j<prices.length; j++) {
                if (prices[i] > prices[j]) {
                    cnt = j;
                    flag = true;
                    break;
                }
            }
            
            if (flag) {
                answer[i] = cnt-i;
            } else {
                answer[i] = (prices.length - 1) - i;
            }
        }
        
        
        return answer;
    }
}