import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
	arr.append(int(input()))

arr.sort()

result = 0
for i in range(1, n+1):
	result += abs(i-arr[i-1])
print(result)