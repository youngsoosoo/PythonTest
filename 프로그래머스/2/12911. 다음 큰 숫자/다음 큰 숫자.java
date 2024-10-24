import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        
        int cnt = countString(Integer.toBinaryString(n));
        
        for (int i=n+1; i<1000001; i++) {
            String temp = Integer.toBinaryString(i);
            
            if (cnt == countString(Integer.toBinaryString(i))) {
                answer = i;
                break;
            }
        }
        
        return answer;
    }
    
    // 문자열 중 1의 개수를 세어주는 함수
    public int countString(String s) {
        int count = 0;
        
        for (int i=0; i<s.length(); i++) {
            if (s.charAt(i) == '1') {
                count++;
            }
        }
        return count;
    }
}