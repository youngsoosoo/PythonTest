import sys
input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

start, end = 0, 0
result = 0
answer = sys.maxsize

while True:
	if result >= s:
		answer = min(answer, end - start)
		result -= arr[start]
		start += 1
	elif end == n:
		break
	else:
		result += arr[end]
		end += 1

if answer == sys.maxsize:
	print(0)
else:
	print(answer)