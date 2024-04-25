import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        int answer = 0;
        int count = 0;
        int idx = 0;
        int end = 0;
        
        Arrays.sort(jobs, (o1, o2) -> o1[0] - o2[0]);
        
        PriorityQueue<int[]> pq = new PriorityQueue<>((o1, o2) -> o1[1] - o2[1]);
        
        while (count < jobs.length) {
            while (idx < jobs.length && jobs[idx][0] <= end) {
                pq.add(jobs[idx++]);
            }
            
            if (pq.isEmpty()) {
                end = jobs[idx][0];
            } else {
                int[] arr = pq.poll();
                answer += arr[1] + end - arr[0];
                end += arr[1];
                count++;
            }
        }
        
        return (int) Math.floor(answer/jobs.length);
    }
}