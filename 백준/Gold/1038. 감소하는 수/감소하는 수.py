import sys
input = sys.stdin.readline

N = int(input())
num = []
answer = []

def check(i):
	global num
	if len(num) == 1:
		return 1
	if num[-2] > i:
		return 1
	else:
		return 0

def dfs(a):
	global num
	for i in range(10):
		num.append(i)
		if check(i):
			dfs(a+1)
			answer.append(int(''.join(str(x) for x in num)))
		num.pop()
		
dfs(0)
answer.sort()

if N >= len(answer):
	print(-1)
else:
	print(answer[N])