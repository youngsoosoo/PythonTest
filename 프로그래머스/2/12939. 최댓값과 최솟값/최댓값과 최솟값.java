import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        
        List<Integer> sToInt = Arrays.stream(s.split("\\s+"))
                                    .map(Integer::parseInt)
                                    .sorted()
                                    .collect(Collectors.toList());
        
        return String.format("%d %d", sToInt.get(0), sToInt.get(sToInt.size() - 1));
    }
}