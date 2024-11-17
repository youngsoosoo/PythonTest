import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        Map<String, Integer> map = new HashMap<>();
        
        for (int i=0; i<want.length; i++) {
            map.put(want[i], number[i]);
        }
        
        Map<String, Integer> discountMap;
        
        for (int i=0; i<discount.length; i++) {
            
            if (discount.length - i < 10) {
                break;
            }
            
            discountMap = new HashMap<>();
            for (int j=i; j<i+10; j++) {
                if (discountMap.containsKey(discount[j])) {
                    discountMap.put(discount[j], discountMap.get(discount[j]) + 1);
                } else {
                    discountMap.put(discount[j], 1);
                }
            }
            
            boolean isBuy = true;
            
            for (int j=0; j<want.length; j++) {
                if (map.get(want[j]) != discountMap.get(want[j])) {
                    isBuy = false;
                }
            }
            
            answer += isBuy ? 1 : 0;
        }

        return answer;
    }
    
    public void print(Map map) {
        System.out.println(map);
    }
    
    public void print(String s) {
        System.out.println(s);
    }
}