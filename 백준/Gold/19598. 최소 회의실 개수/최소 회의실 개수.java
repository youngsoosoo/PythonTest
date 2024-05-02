import java.io.*;
import java.util.*;

class Main {
	
	static class Time implements Comparable<Time> {
		int time;
		boolean isTime;
		
		public Time(int time, boolean isTime) {
			this.time = time;
			this.isTime = isTime;
		}
		
		@Override
		public int compareTo(Time t) {
			return this.time - t.time;
		}
	}
	
	static PriorityQueue<Time> pq;
	
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int answer = 0;
		
		int n = Integer.parseInt(br.readLine());
		pq = new PriorityQueue<>();
		
		StringTokenizer st;
		
		for(int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			pq.offer(new Time(Integer.parseInt(st.nextToken()), true));
			pq.offer(new Time(Integer.parseInt(st.nextToken()), false));
		}
		
		int cnt = 0;
		
		while (!pq.isEmpty()) {
			Time t = pq.poll();
			
			if (t.isTime) {
				cnt++;
				answer = Math.max(answer, cnt);
			} else {
				cnt--;
			}
		}
		
		System.out.println(answer);
	}
}