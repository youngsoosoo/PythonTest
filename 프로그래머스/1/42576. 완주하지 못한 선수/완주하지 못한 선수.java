import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> map = new HashMap<>();
        
        for (String parti : participant) {
            map.put(parti, map.getOrDefault(parti, 0) + 1);
        }
        for (String compl : completion) {
            map.put(compl, map.get(compl) - 1);
        }
        
        for (String parti : participant) {
            if (map.get(parti) >= 1) {
                return parti;
            }
        }
        
        return answer;
    }
}