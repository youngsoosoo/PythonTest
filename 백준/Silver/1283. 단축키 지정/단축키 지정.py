import sys
input = sys.stdin.readline

n = int(input())
result = []

for _ in range(n):
	s = list(input().split())
	
	flag = False
	for i in range(len(s)):
		if s[i][0].upper() not in result:
			result.append(s[i][0].upper())
			flag = True
			s[i] = '[' + s[i][0] + ']' + s[i][1:]
			print(' '.join(s))
			break
	
	if not flag:
		for i in range(len(s)):
			_flag = False
			for j in range(len(s[i])):
				if s[i][j].upper() not in result:
					result.append(s[i][j].upper())
					flag = True
					_flag = True
					s[i] = s[i][:j] + '[' + s[i][j] + ']' + s[i][j+1:]
					print(' '.join(s))
					break
			if _flag:
				break
	
	if not flag:
		print(' '.join(s))