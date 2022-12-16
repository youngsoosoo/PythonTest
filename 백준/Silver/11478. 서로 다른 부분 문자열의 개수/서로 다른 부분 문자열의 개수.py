import sys
input = sys.stdin.readline

s = input()
cnt=set()

for i in range(len(s)):
	for j in range(len(s)):
		if i+j <len(s):
			cnt.add(s[i:i+j])
print(len(cnt)-1)