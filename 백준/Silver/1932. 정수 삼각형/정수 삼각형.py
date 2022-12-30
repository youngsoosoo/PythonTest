import sys
input = sys.stdin.readline

n=int(input())
semo = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
	for j in range(len(semo[i])):
		a=0
		if j==len(semo[i])-1:
			semo[i][j] += semo[i-1][-1]
		else:
			if j!=0:
				semo[i][j]=max(semo[i][j]+semo[i-1][j-1], semo[i][j]+semo[i-1][j])
			else:
				semo[i][j]+=semo[i-1][j]

print(max(semo[n-1]))