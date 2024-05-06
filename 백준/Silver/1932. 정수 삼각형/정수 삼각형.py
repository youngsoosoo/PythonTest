import sys
input = sys.stdin.readline

n = int(input())

semo = [list(map(int, input().split())) for i in range(n)]

for i in range(1, n):
	for j in range(len(semo[i])):
		if j == 0:
			semo[i][j] += semo[i-1][0]
		elif j == len(semo[i])-1:
			semo[i][j] += semo[i-1][-1]
		else:
			semo[i][j] += max(semo[i-1][j-1], semo[i-1][j])
	
print(max(semo[-1]))