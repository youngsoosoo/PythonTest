import java.util.*;

class Solution {
    public int solution(int[][] maps) {
        int[][] d = {{1, 0}, {-1, 0}, {0, -1}, {0, 1}};
        Queue<int[]> queue = new ArrayDeque<>();
        queue.add(new int[]{0, 0});
        
        int xLength = maps.length;
        int yLength = maps[0].length;

        while (!queue.isEmpty()) {
            int[] location = queue.poll();
            int x = location[0];
            int y = location[1];

            if (x == xLength - 1 && y == yLength - 1) {
                return maps[x][y];
            }

            for (int i = 0; i < 4; i++) {
                int dx = x + d[i][0];
                int dy = y + d[i][1];

                if (dx >= 0 && dx < xLength && dy >= 0 && dy < yLength && maps[dx][dy] == 1) {
                    maps[dx][dy] = maps[x][y] + 1;
                    queue.add(new int[]{dx, dy});
                }
            }
        }

        return -1;
    }
}