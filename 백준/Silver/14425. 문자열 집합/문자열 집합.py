import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [input().strip() for i in range(n)]
arr1 = [input().strip() for i in range(m)]
cnt = 0
for i in arr1:
	if i in arr:
		cnt+=1
print(cnt)