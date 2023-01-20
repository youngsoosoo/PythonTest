import sys
input = sys.stdin.readline

n = int(input())
dis = list(map(int, input().split()))
pwd = list(map(int, input().split()))

r=0
m=pwd[0]
for i in range(n-1):
	if pwd[i] < m:
		m = pwd[i]
	r += m * dis[i]

print(r)