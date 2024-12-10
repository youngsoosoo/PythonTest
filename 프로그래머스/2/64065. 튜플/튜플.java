import java.util.*;

class Solution {
    public int[] solution(String s) {
        s = s.substring(2, s.length()-2);
        String[] text = s.split("},\\{");
        
        List<int[]> list = new ArrayList<>();
            
        for (String t : text) {
            int[] numbers = Arrays.stream(t.split(","))
                                  .mapToInt(Integer::parseInt)
                                  .toArray();
            list.add(numbers);
        }
        
        list.sort(Comparator.comparingInt(temp -> temp.length));
        
        List<Integer> answer = new ArrayList<>();
        
        for(int i=0; i<list.size(); i++) {
            for (int j=0; j<list.get(i).length; j++){
                if (!answer.contains(list.get(i)[j])) {
                    answer.add(list.get(i)[j]);
                }
            }
        }
        
        return answer.stream().mapToInt(i -> i).toArray();
    }
}