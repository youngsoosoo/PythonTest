import java.io.*;
import java.util.*;

class Main {
	
	static int [][] dp = new int[30][30];
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		
		StringTokenizer st;
		StringBuilder sb = new StringBuilder();
		
		for(int i = 0; i < n; i++) {
			st = new StringTokenizer(br.readLine(), " ");
			
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			sb.append(combination(b, a)).append('\n');
		}
		
		System.out.println(sb);
	}
	
	static int combination(int a, int b) {
		if(dp[a][b] > 0) {
			return dp[a][b];
		}
		
		else if(a == b || b == 0) {
			return dp[a][b] = 1;
		}
		
		else{
			return dp[a][b] = combination(a-1, b-1) + combination(a-1, b);
		}
	}
}