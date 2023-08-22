import sys
input = sys.stdin.readline

n = 0
n_idx = 0
arr = [0 for i in range(1001)]

# 가장 큰 기둥을 찾아 왼쪽과 오른쪽으로 나눈 후 값을 계산
for i in range(int(input())):
	x, y = map(int, input().split())
	arr[x] = y
	if n < y:
		n_idx = x
		n = y

answer = 0

# 왼쪽 값 계산
m = 0
for i in range(n_idx+1):
	m = max(m, arr[i])
	answer += m

# 오른쪽 값 계산
m = 0
for i in range(1000, n_idx, -1):
	m = max(m, arr[i])
	answer += m

print(answer)