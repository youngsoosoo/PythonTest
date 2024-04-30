import java.io.*;
import java.util.*;

class Main {
	
	static int nx, ny;
	
	static class Node {
		int x;
		int y;
		
		public Node(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	public static int solution(int[][] graph, int x, int y) {
		
		// 섬의 개수
		int answer = 0;
		
		int[][] d = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}, {1, 1}, {-1, -1}, {-1, 1}, {1, -1}};
		boolean[][] visited = new boolean[x][y];
		Queue<Node> q = new LinkedList<>();
		
		for(int i=0; i<x; i++) {
			for(int j=0; j<y; j++) {
				
				if (!visited[i][j] && graph[i][j] == 1) {
					visited[i][j] = true;
					q.offer(new Node(i, j));
					answer++;
				}
				
				while (!q.isEmpty()) {
					Node node = q.poll();
					
					for (int k=0; k<8; k++) {
						nx = d[k][0] + node.x;
						ny = d[k][1] + node.y;
						
						if(0 <= nx && nx < x && 0 <= ny && ny < y && !visited[nx][ny] && graph[nx][ny] == 1) {
							visited[nx][ny] = true;
							q.offer(new Node(nx, ny));
						}
					}
				}
			}
		}
		return answer;
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		while (true) {
			String[] line = br.readLine().split(" ");
			int y = Integer.parseInt(line[0]);
			int x = Integer.parseInt(line[1]);
			
			if (x == 0 && y == 0) break;
			
			int[][] graph = new int[x][y];
			
			for(int i=0; i<x; i++) {
				String[] nline = br.readLine().split(" ");
				for(int j=0; j<y; j++) {
					graph[i][j] = Integer.parseInt(nline[j]);
				}
			}
			
			sb.append(solution(graph, x, y)).append('\n');
		}
		System.out.println(sb);
	}
}