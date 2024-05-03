import java.io.*;
import java.util.*;

class Main {
	
	static int n;
	static int m;
	static int answer = Integer.MAX_VALUE;
	
	static int[][] graph;
	
	// 바이러스 놓을 수 있는 위치
	static ArrayList<Coordinate> arr;
	
	// m개 선택된 바이러스 위치
	static Coordinate[] choice;
	
	static int[][] d = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
	
	static class Coordinate {
		int x;
		int y;
		
		public Coordinate(int x, int y) {
			this.x = x;
			this.y = y;
		}
	}
	
	public static void dfs(int idx, int j) {
		
		if (idx == m) {
			bfs();
			return;
		}
		
		for (int i=j; i<arr.size(); i++) {
			choice[idx] = arr.get(i);
			dfs(idx+1, i+1);
		}
	}
	
	public static void bfs() {
		
		Queue<Coordinate> q = new LinkedList<>();
		boolean[][] visited = new boolean[n][n];
		int result = 0;
		
		for (Coordinate coordinate : choice) {
			visited[coordinate.x][coordinate.y] = true;
			q.offer(coordinate);
		}
		
		while (!q.isEmpty()) {
			if (result >= answer) return;
			
			int size = q.size();
			for (int i = 0; i<size; i++) {
				Coordinate coordinate = q.poll();
				
				for (int j=0; j<4; j++) {
					int nx = coordinate.x + d[j][0];
					int ny = coordinate.y + d[j][1];
					if ((0<=nx && nx<n && 0<=ny && ny<n) && !visited[nx][ny]) {
						
						if (graph[nx][ny] != 1) {
							visited[nx][ny] = true;
							q.offer(new Coordinate(nx, ny));
						}
					}
				}
			}
			
			result++;
		}
		boolean flag = true;
		for(int i=0;i<n;i++){
			for(int j=0;j<n;j++){
				if (graph[i][j] != 1 && !visited[i][j]) {
					flag = false;
					break;
				}
			}
			if (!flag) break;
		}
		
		if (flag) {
			answer = Math.min(answer, result-1);
		}
	}
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		graph = new int[n][n];
		arr = new ArrayList<>();
		
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<n; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
				if (graph[i][j] == 2) {
					arr.add(new Coordinate(i, j));
				}
			}
		}
		
		choice = new Coordinate[m];
		dfs(0, 0);
		
		if (answer == Integer.MAX_VALUE) System.out.println(-1);
		else System.out.println(answer);
	}
}