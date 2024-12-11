import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        List<String> list1 = stringSplit(str1);
        List<String> list2 = stringSplit(str2);
        
        if (list1.isEmpty() && list2.isEmpty()) {
            return 65536;
        }
        
        List<String> union = new ArrayList<>();
        List<String> inter = new ArrayList<>();
        
        for (String s : list1) {
            if (list2.remove(s)) {
                inter.add(s);
            }
            
            union.add(s);
        }
        
        union.addAll(list2);
        
        return (int) (((double) inter.size() / (double) union.size()) * 65536);
    }
    
    public List<String> stringSplit(String s) {
        List<String> list = new ArrayList<>();
        s = s.toLowerCase();
        
        for (int i=0; i<s.length()-1; i++) {
            String str = s.substring(i, i+2).replaceAll("[^a-z]", "");
            
            if (str.length() == 2) {
                list.add(str);
            }
        }
        
        return list;
    }
}