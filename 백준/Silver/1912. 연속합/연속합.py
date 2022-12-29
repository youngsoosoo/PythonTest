import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
li =[arr[0]]

for i in range(len(arr)-1):
	li.append(max(li[i] + arr[i+1], arr[i+1]))
print(max(li))