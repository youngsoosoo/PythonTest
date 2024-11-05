import java.util.*;

// 반으로 나눴을 때 다른 곳에 있다면
// N = 2 이면 1 경기
// N = 4 이면 2 경기
// N = 8 이면 3 경기
// N = 16 이면4 경기
// ...

// 홀수면 +1 / 2, 짝수면 /2


class Solution
{
    public int solution(int n, int a, int b)
    {
        return recur(n, a, b, 0);
    }
    
    public int recur(int n, int a, int b, int c) {
        if (a==b) {
            return c;
        }
        
        // 경기 수 증가
        c++;
        
        a = (a%2) == 0 ? a/2 : (a + 1) / 2;
        b = (b%2) == 0 ? b/2 : (b + 1) / 2;

        // 재귀 호출
        return recur(n, a, b, c);
    }
}