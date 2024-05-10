import sys
input = sys.stdin.readline

answer = 0
n, t, p = map(int, input().split())

times = []
visited = [[[0 for i in range(101)] for j in range(60)] for k in range(22)]

for _ in range(t):
	start, end = map(int, input().split())
	startT, startM = start//100, start%100
	endT, endM = end//100, end%100
	times.append([[startT, startM], [endT, endM]])
times.sort()

for time in times:
	startT, startM, endT, endM = time[0][0], time[0][1], time[1][0], time[1][1]
	
	max_dis = 0
	idx = 0
	
	# 비어있는 자리 확인
	for i in range(1, n+1):
		if not visited[startT][startM][i]:
			dis = 101;
			for j in range(1, n+1):
				# j에 사람이 있는지 확인 후 거리 계산
				if i != j and visited[startT][startM][j]:
					dis = min(dis, abs(i-j))
			
			if dis > max_dis:
				idx = i
				max_dis = dis
	
	for t in range(startT, endT+1):
		if startT == endT:
			for m in range(startM, endM):
				visited[t][m][idx] = 1
			break
		
		if t == startT:
			for m in range(startM, 60):
				visited[t][m][idx] = 1
				
		elif t == endT:
			for m in range(endM):
				visited[t][m][idx] = 1
		else:
			for m in range(60):
				visited[t][m][idx] = 1
a =0
for t in range(9, 21):
	for m in range(60):
		a += 1
		if not visited[t][m][p]:
			answer+=1
print(answer)
