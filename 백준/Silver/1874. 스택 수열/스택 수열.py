import sys
input = sys.stdin.readline

n = int(input())
stk = []
arr = []
cnt=1
for i in range(n):
	a = int(input())
	
	while cnt <= a:
		stk.append(cnt)
		arr.append("+")
		cnt+=1
	if stk[-1] == a:
		stk.pop()
		arr.append("-")
	else:
		arr.append("NO")
		break

if arr[-1] != "NO":
	for i in arr:
		print(i)
else:
	print(arr[-1])	
	