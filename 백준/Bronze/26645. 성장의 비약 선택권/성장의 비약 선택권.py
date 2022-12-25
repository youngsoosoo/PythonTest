import sys
input = sys.stdin.readline

n=int(input())

if n<210:
	if n>=206:
		print(2)
	else:
		print(1)
elif n<220:
	if n>217	:
		print(3)
	else:
		print(2)
elif n<230:
	if n==229:
		print(4)
	else:
		print(3)
else:
	print(4)