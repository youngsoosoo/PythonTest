import sys
input = sys.stdin.readline

s = input().split('-')
arr=[]
for i in s:
	a=0
	ss = i.split('+')
	for j in ss:
		a+=int(j)
	arr.append(a)

n=arr[0]
for i in range(1, len(arr)):
	n-=arr[i]

print(n)