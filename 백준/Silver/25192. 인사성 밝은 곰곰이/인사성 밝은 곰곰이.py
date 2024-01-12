import sys
input = sys.stdin.readline

N = int(input())
str(input())
cnt = 0
dic = {}

for _ in range(N-1):
	s = str(input()).rstrip()
	
	if s == "ENTER":
		for key, value in dic.items():
			if value == 1:
				cnt += 1
		dic = {}
		continue
		
	if s not in dic:
		dic[s] = 1
		
for key, value in dic.items():
		if value == 1:
			cnt += 1
	
print(cnt)