import java.util.*;
class Solution {
    public int solution(int n) {
        int[] iList = new int[1000001];
        
        iList[0] = 0;
        iList[1] = 1;
        
        for (int i = 2; i < n+1; i++) {
            iList[i] = (iList[i-1] + iList[i-2]) % 1234567;
        }
        
        return iList[n];
    }
}