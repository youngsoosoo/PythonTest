import sys
input = sys.stdin.readline

s = input().strip()
cnt=set()

for i in range(len(s)):
	for j in range(i, len(s)):
		cnt.add(s[i:j+1])
print(len(cnt))