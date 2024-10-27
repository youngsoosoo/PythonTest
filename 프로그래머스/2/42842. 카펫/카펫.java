class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = {0, 0};
        
        for(int i=3; i<brown+yellow; i++) {
            int x = (brown+yellow) / i;
            if (x >= i && ((i-2) * (x-2) == yellow)) {
                answer[0] = x;
                answer[1] = i;
                break;
            }
        }
        
        return answer;
    }
}