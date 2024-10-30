import java.util.*;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = {0, 0};
        List<String> list = new ArrayList<>();
        
        for(int i=0;i<words.length; i++) {
            if (list.contains(words[i]) || (i > 0 && words[i].charAt(0) != words[i-1].charAt(words[i-1].length() - 1))) {
                answer[0] = (i%n) + 1;
                answer[1] = (i/n) + 1;
                return answer;
            }
            
            list.add(words[i]);
        }
        
        return new int[]{0, 0};
    }
}