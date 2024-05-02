import java.io.*;
import java.util.*;

class Main {
	
	public static final int INF = Integer.MAX_VALUE;
	
	static int[][] graph;
	static int[] distance;
	static int[][] answer;
	static int n;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		graph = new int[n+1][n+1];
		for(int i=1; i<=n; i++) {
			st = new StringTokenizer(br.readLine());
			for(int j=1; j<=n; j++) {
				graph[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		
		answer = new int[n+1][n+1];
		
		for(int i=0; i<m; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int time = Integer.parseInt(st.nextToken());
			
			if (answer[start][end] != 0) {
				if (answer[start][end] <= time) {
					System.out.println("Enjoy other party");
				} else{
					System.out.println("Stay here");
				}
			}else {
				if (dik(start, end) <= time) {
					System.out.println("Enjoy other party");
				} else{
					System.out.println("Stay here");
				}
			}
		}
	}
	
	public static int dik(int start, int end) {
		int[] distance = new int[n+1];
		Arrays.fill(distance, INF);
		distance[start] = 0;
		
		PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[0] - b[0]);
		pq.offer(new int[]{0, start});
		
		while (!pq.isEmpty()) {
			int[] data = pq.poll();
			if (distance[data[1]] < data[0]){
				continue;
			}
			
			for(int i=1; i<=n; i++) {
				int cost = data[0] + graph[data[1]][i];
				
				if (cost<distance[i]) {
					distance[i] = cost;
					pq.offer(new int[]{cost, i});
				}
			}
		}
		
		answer[start] = distance;
		return distance[end];
	}
}