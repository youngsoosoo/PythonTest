import sys
input = sys.stdin.readline

n, k = map(int, input().split())
krr = list(map(int, input().split()))
arr=[sum(krr[:k])]

for i in range(n-k):
	arr.append(arr[i] - krr[i] + krr[k+i])
print(max(arr))