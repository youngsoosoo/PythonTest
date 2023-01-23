import sys
input = sys.stdin.readline

while True:
	s = input().rstrip()
	if s == '.':
		break
	
	a=[]
	b = True
	
	for i in s:
		if i == '(' or i == '[':
			a.append(i)
		elif i == ')':
			if len(a) == 0 or a[-1] == '[':
				b = False
				break
			elif a[-1] == '(':
				a.pop()
		elif i == ']':
			if len(a) == 0 or a[-1] == '(':
				b = False
				break
			elif a[-1] == '[':
				a.pop()
	if b == True and not a:
		print('yes')
	else:
		print('no')