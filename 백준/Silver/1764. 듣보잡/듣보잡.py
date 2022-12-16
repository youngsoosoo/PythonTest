import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = set()
for i in range(n):
	arr1.add(input().strip())
	
arr2 = set()
for i in range(m):
	arr2.add(input().strip())

result = sorted(list(arr1 & arr2))

print(len(result))
for i in result:
	print(i)