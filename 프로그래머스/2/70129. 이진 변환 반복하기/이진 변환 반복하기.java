import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = {0, 0};
        int count = 0;
        int zeroCount = 0;
        String alpha = "";
        int len = s.length();
        
        while (s.length() > 1) {
            zeroCount = 0;
            count = 0;
            len = s.length();
            
            for (int i=0; i<len; i++) {
                if (s.charAt(i) == '1') {
                    count++;
                } else {
                    zeroCount++;
                }
            }
            
            answer[0] += 1;
            answer[1] += zeroCount;
            s = convertToBase(count, 2);
        }
        
        return answer;
    }
    
    public String convertToBase(int number, int base) {
        
        StringBuilder result = new StringBuilder();
        
        while(number > 0) {
            result.append(number % base);
            number /= base;
        }
        
        return result.toString();
    }
}