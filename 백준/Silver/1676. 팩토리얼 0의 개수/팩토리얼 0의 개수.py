import sys
from math import factorial
input = sys.stdin.readline

a = factorial(int(input()))
a="".join(reversed(str(a)))
cnt=0
for i in range(len(a)):
	if a[i] != '0':
		break
	else:
		cnt+=1
print(cnt)