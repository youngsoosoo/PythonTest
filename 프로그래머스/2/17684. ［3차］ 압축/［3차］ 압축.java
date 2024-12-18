import java.util.*;

class Solution {
    public int[] solution(String msg) {
        List<Integer> answer = new ArrayList<>();
        Map<String, Integer> map = new HashMap<>();
        
        for (int i = 1; i <= 26; i++) {
            char letter = (char) ('A' + i - 1); // A의 ASCII 값에서 i-1만큼 더함
            map.put(String.valueOf(letter), i);
        }
        
        if (msg.length() == 1) {
            answer.add(map.get(msg));
        }
        
        int cnt = 0;
        
        while (cnt < msg.length()) {
            
            String key = String.valueOf(msg.charAt(cnt));
            
            if (map.containsKey(key)) {
                int flagCnt = 0;
                
                for (int j=cnt+1; j<msg.length(); j++) {
                    flagCnt++;
                    if (map.containsKey(key + String.valueOf(msg.charAt(j)))) {
                        key += String.valueOf(msg.charAt(j));
                    } else {
                        answer.add(map.get(key));
                        map.put(key + String.valueOf(msg.charAt(j)), map.size()+1);
                        break;
                    }
                }
                
                if (flagCnt > 1) {
                    cnt += flagCnt;
                } else {
                    cnt++;
                }
                
                if (map.containsKey(msg.substring(cnt, msg.length()))) {
                    answer.add(map.get(msg.substring(cnt, msg.length())));
                    break;
                }
            }
        }
        
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}