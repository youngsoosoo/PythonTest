import sys, heapq
input = sys.stdin.readline

for _ in range(int(input())):
	n, d, c = map(int, input().split())
	graph = [[] for i in range(n+1)]
	time = [sys.maxsize for _ in range(n+1)]
	q = []
	
	
	for _ in range(d):
		# a -> b
		a, b, s = map(int, input().split())
		graph[b].append([a, s])
	
	heapq.heappush(q, [c, 0])
	time[c] = 0
	while q:
		cnode, ctime = heapq.heappop(q)
		
		for nnode, ntime in graph[cnode]:
			if ctime + ntime < time[nnode]:
				time[nnode] = ctime + ntime
				heapq.heappush(q, [nnode, time[nnode]])
	
	answer = 0
	max_time = 0
	
	for t in time:
		if sys.maxsize != t:
			answer += 1
			max_time = max(max_time, t)
	print(answer, max_time)