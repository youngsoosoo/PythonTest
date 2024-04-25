import java.util.*;
class Solution {
    public int solution(int[][] sizes) {
        
        int max_i = 0;
        int max_j = 0;
        
        for (int[] size:sizes) {
            
            if (size[0] >= size[1]) {
                max_i=Math.max(max_i, size[0]);
                max_j=Math.max(max_j, size[1]);
            } else {
                max_i=Math.max(max_i, size[1]);
                max_j=Math.max(max_j, size[0]);
            }
        }
        
        return max_i * max_j;
    }
}