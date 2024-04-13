import java.util.*;
class Solution {
    public ArrayList solution(int[] progresses, int[] speeds) {
        ArrayList<Integer> answer = new ArrayList<Integer>();
        Queue<Integer> q = new LinkedList<Integer>();
        
        for (int i=0; i<progresses.length; i++) {
            q.add((int)Math.ceil((100.0-progresses[i])/speeds[i]));
        }
        
        while(!q.isEmpty()) {
            int minDays = q.poll();
            int count = 1;
            
            while (!q.isEmpty() && q.peek() <= minDays) {
                q.poll();
                count++;
            }
            
            answer.add(count);
        }
        
        
        return answer;
    }
}