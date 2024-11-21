import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> list = new ArrayList<>();
        int n = progresses.length;
        
        // 각 작업의 완료 시간을 계산
        int[] completionTimes = new int[n];
        
        for (int i = 0; i < n; i++) {
            int remaining = 100 - progresses[i];
            completionTimes[i] = (remaining + speeds[i] - 1) / speeds[i]; // 올림 계산
        }
        
        // 배포할 작업 수 계산
        int count = 0;
        int maxTime = completionTimes[0];
        
        for (int i = 0; i < n; i++) {
            if (completionTimes[i] <= maxTime) {
                count++;
            } else {
                list.add(count); // 이전 작업 수 추가
                count = 1; // 새로운 작업 시작
                maxTime = completionTimes[i]; // 새로운 최대 시간 업데이트
            }
        }
        
        // 마지막 작업 수 추가
        if (count > 0) {
            list.add(count);
        }
        
        // 결과를 int[]로 변환
        int[] answer = list.stream()
                          .mapToInt(Integer::intValue)
                          .toArray();
        
        return answer;
    }
}