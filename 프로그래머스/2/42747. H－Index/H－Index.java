class Solution {
    public int solution(int[] citations) {
        int answer = 0;
        
        int a;
        int b;
        
        for (int i=0; i<10001; i++) {
            // a는 i번 이상 인용된 논문의 수
            a = 0;
            // b는 i번 이하 인용된 논문의 수
            b = 0;
            
            for (int j=0; j<citations.length; j++) {
                
                if (citations[j] >= i) {
                    a+=1;
                }
                if (citations[j] <= i) {
                    b+=1;
                }
            }
            
            if (a >= i) {
                answer = i;
            }
        }
        
        return answer;
    }
}