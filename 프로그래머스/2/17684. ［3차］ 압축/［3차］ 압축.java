import java.util.*;

class Solution {
    public int[] solution(String msg) {
        List<Integer> answer = new ArrayList<>();
        Map<String, Integer> map = makeDict();
        
        // 현재 msg 문자열의 가르키고(Cursor) 있는 곳의 위치
        int cnt = 0;
        
        while (cnt < msg.length()) {
            // Key 초기화
            String key = "";
            
            // 문자열을 순회하며 사전에 없는 글자 탐색
            for (int i=cnt; i<msg.length(); i++) {
                // 사전에 존재하지 않는 글자가 나오면 사전에 추가하고 탈출
                if (!map.containsKey(key + msg.charAt(cnt))) {
                    map.put(key + msg.charAt(cnt), map.size()+1);
                    break;
                // 사전에 존재하는 글자는 문자열에 문자를 추가하며 순회
                } else {
                    key += msg.charAt(cnt);
                }
                cnt ++;
            }
            // 사전에서 색인 번호를 찾아 출력
            answer.add(map.get(key));
        }
        
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
    
    // 사전 제작
    public Map<String, Integer> makeDict() {
        Map<String, Integer> map = new HashMap<>();
        
        for (int i = 1; i <= 26; i++) {
            char letter = (char) ('A' + i - 1); // A의 ASCII 값에서 i-1만큼 더함
            map.put(String.valueOf(letter), i);
        }
        
        return map;
    }
}