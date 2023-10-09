import sys
input = sys.stdin.readline

a, b, n, w = map(int, input().split())
cnt = 0
answer1, answer2 = 0, 0
flag = 0
for i in range(1, n):
	if a*i + b*(n-i) == w:
		cnt += 1
		answer1, answer2 = i, n-i
		flag=1

if cnt == 1 and flag == 1:
	print(answer1, answer2)
else:
	print(-1)