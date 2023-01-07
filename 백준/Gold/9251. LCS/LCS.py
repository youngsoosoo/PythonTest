import sys
input = sys.stdin.readline

str1, str2 = input().strip(), input().strip()
h, w = len(str1), len(str2)
arr = [[0] * (w+1) for _ in range(h+1)]

for i in range(1, h+1):
	for j in range(1, w+1):
		if str1[i-1] == str2[j-1]:
			arr[i][j] = arr[i-1][j-1] + 1
		else:
			arr[i][j] = max(arr[i][j-1], arr[i-1][j])
print(arr[-1][-1])