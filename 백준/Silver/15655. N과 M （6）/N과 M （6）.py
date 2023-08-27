import sys
input = sys.stdin.readline

def recur(number):
	if number == m:
		print(*answer)
		return
	for i in arr:
		if i in answer or (answer and answer[-1] >= i):
			continue
		answer.append(i)
		recur(number+1)
		answer.pop()

n, m = map(int, input().split())
arr = list(map(int ,input().split()))
answer = []

arr.sort()

recur(0)