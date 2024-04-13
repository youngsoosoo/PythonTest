import java.util.*;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        PriorityQueue<Integer> q = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int i : priorities) {
            q.offer(i);
        }
        
        while (!q.isEmpty()) {
            for (int i=0; i < priorities.length; i++) {
                if (q.peek() == priorities[i]){
                    q.poll();
                    answer++;
                    
                    if (location == i) {
                        return answer;
                    }
                }
            }
        }
        
        return answer;
    }
}