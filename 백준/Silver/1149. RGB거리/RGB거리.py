import sys
input = sys.stdin.readline
#빨 초 파
n=int(input())
rgb = [list(map(int,input().split())) for i in range(n)]
for i in range(1, len(rgb)):
	rgb[i][0]=min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
	rgb[i][1]=min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
	rgb[i][2]=min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]
print(min(rgb[n-1]))