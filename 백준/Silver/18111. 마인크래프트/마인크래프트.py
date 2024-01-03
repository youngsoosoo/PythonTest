import sys
input = sys.stdin.readline

N, M, B = map(int, input().split())
graph = []
high = 0

for _ in range(N):
	graph.extend(map(int ,input().split()))

time = [0 for i in range(257)]
for n in range(257):
	block = B
	for j in graph:
		if j <= n:
			time[n] += n-j
			block -= n-j
		else:
			time[n] += 2 * (j-n)
			block += j-n
			
	if block >= 0 and time[n] <= time[high]:
		high = n
		
print(time[high], high)