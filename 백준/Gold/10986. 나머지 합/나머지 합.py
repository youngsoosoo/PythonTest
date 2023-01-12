import sys
input = sys.stdin.readline

n , m = map(int, input().split())
nrr = list(map(int, input().split()))
arr=[0]*m
arr[0] = 1
a=0
for i in range(n):
	a += nrr[i]
	arr[a%m]+=1
a=0
for i in arr:
	a+=i*(i-1)//2
	
print(a)
