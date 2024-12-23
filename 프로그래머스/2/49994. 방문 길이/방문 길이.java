import java.util.*;

class Solution {
    private static int nx[] = {-1, 0, 1, 0};
    private static int ny[] = {0, -1, 0, 1};
    
    public int solution(String dirs) {
        int answer = 0;
        int len = dirs.length();
        
        boolean[][][] visited = new boolean[11][11][4];
        int x = 5, y = 5;
        
        for (int i=0; i<len; i++) {
            char c = dirs.charAt(i);
            int d = 0;
            if (dirs.charAt(i) == 'U') {
                d = 0;
            } else if (dirs.charAt(i) == 'L') {
                d = 1;
            } else if (dirs.charAt(i) == 'D') {
                d = 2;
            } else {
                d = 3;
            }
            
            int dx = x + nx[d];
            int dy = y + ny[d];
            
            if (dx >= 11 || dx < 0 || dy >= 11 || dy < 0) {
                continue;
            }
            
            if (!visited[dx][dy][d]) {
                answer += 1;
                visited[dx][dy][d] = true;
                d = (d%2 == 0) ? 2-d:4-d;
                visited[x][y][d] = true;
            }
            x = dx;
            y = dy;
        }
        
        return answer;
    }
}