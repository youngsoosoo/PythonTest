import java.util.*;

class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        
        if (cacheSize == 0) {
            return 5 * cities.length;
        }
        
        List<String> list = new ArrayList<>();
        boolean isList = false;
        
        for (int i=0; i<cities.length; i++) {
            cities[i] = cities[i].toLowerCase();
            isList = false;
            
            for(int j=0; j<list.size(); j++) {
                if (list.get(j).equals(cities[i])) {
                    isList = true;
                    list.remove(j);
                    break;
                }
            }
            
            if (isList) {
                answer += 1;
            } else {
                answer += 5;
                if (list.size() >= cacheSize) {
                    list.remove(0);
                }
            }
            list.add(cities[i]);
        }
        
        return answer;
    }
}