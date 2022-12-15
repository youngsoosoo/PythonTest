import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [input().strip() for i in range(n)]
arr_num = {(i + 1): arr[i] for i in range(0, len(arr))}
arr_str = {arr[i]:(i + 1) for i in range(0, len(arr))}

for i in range(m):
	arr1 = input().strip()
	if arr1.isdigit():
		print(arr_num[int(arr1)])
	else:
		print(arr_str[arr1])