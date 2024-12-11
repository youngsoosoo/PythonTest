class Solution {
    int[] numberList;
    int targerNumber;
    
    public int solution(int[] numbers, int target) {
        numberList = numbers;
        targerNumber = target;
        
        return dfs(0, 0);
    }
    
    public int dfs(int cnt, int result) {
        
        if (cnt >= numberList.length) {
            if (targerNumber == result) {
                return 1;
            }
            return 0;
        }
        
        int answer = 0;
        
        answer += dfs(cnt + 1, result - numberList[cnt]);
        answer += dfs(cnt + 1, result + numberList[cnt]);
            
        return answer;
    }
}