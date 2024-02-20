import sys
input = sys.stdin.readline

t = int(input())
arr = [0, 0] + [1] * 999999

for i in range(2, 1000001):
	if arr[i]:
		for j in range(2*i, 1000001, i):
			arr[j] = 0

for i in range(t):
	answer = 0
	n = int(input())
	for j in range(2, n//2+1):
		if arr[j] and arr[n-j]:
			answer+=1
	print(answer)