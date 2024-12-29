import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;
        
        PriorityQueue<Integer> hq = new PriorityQueue<>();
        
        for (int i=0; i<scoville.length; i++) {
            hq.add(scoville[i]);
        }
        
        while (true) {
            
            if (hq.size() < 2 && hq.peek() < K) {
                answer = -1;
                break;
            }
            
            if (hq.peek() >= K) {
                break;
            }
            
            int min1 = hq.poll();
            int min2 = hq.poll();
            
            hq.offer(min1 + (min2 * 2));
            answer++;
        }
        
        return answer;
    }
}