import java.util.*;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        // Stack 활용
        Stack<Integer> stack = new Stack<>();
        // 첫 번째 수
        stack.push(0);
        
        for (int i=1; i<numbers.length; i++) {
            // stack에 값이 존재할 때, stack에 저장된 아직 큰 값을 찾지 못한 수와 현재 위치의 수를 비교를 반복함.
            while(!stack.isEmpty() && numbers[stack.peek()] < numbers[i]) {
                // 큰 값으로 result 출력
                answer[stack.pop()] = numbers[i];
            }
            
            // 현재 수도 비교해주기 위해 push
            stack.push(i);
        }
        
        // 큰 값을 발견하지 못한 값들 -1 처리
        while(!stack.isEmpty()) {
            answer[stack.pop()] = -1;
        }
        
        return answer;
    }
}