import sys
input = sys.stdin.readline
	

n, m = map(int, input().split())
b = list(map(int, input().split()))
a=[]
for i in range(n):
	for j in range(i+1, n):
		for k in range(j+1, n):
			if b[i] + b[j] + b[k]>m:
				continue
			else:
				a.append(b[i] + b[j] + b[k])

print(max(a))