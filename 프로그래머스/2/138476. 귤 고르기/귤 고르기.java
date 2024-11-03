import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        Map<Integer, Integer> map = new HashMap<>();
        
        for (int i=0; i<tangerine.length; i++) {
            map.put(tangerine[i], map.getOrDefault(tangerine[i], 0) + 1);
        }
        
        Collection<Integer> values = map.values();
        
        // Collection을 List로 변환
        List<Integer> valueList = new ArrayList<>(values);

        // 값 정렬 (내림차순)
        Collections.sort(valueList, Collections.reverseOrder());
        
        for (int i=0; i<valueList.size(); i++) {
            if (k-valueList.get(i) <= 0) {
                answer+=1;
                break;
            }
            k-=valueList.get(i);
            answer+=1;
        }
        
        return answer;
    }
}