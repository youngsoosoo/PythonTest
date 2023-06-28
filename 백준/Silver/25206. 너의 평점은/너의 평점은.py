import sys
input = sys.stdin.readline

result = 0.0
s = 0.0
for i in range(20):
	a, b, c = map(str, input().split())
	b = float(b)
	
	if c != 'P':
		s+=b
		if c == 'A+':
			result += 4.5*b
		elif c == 'A0':
			result += 4.0*b
		elif c == 'B+':
			result += 3.5*b
		elif c == 'B0':
			result += 3.0*b
		elif c == 'C+':
			result += 2.5*b
		elif c == 'C0':
			result += 2.0*b
		elif c == 'D+':
			result += 1.5*b
		elif c == 'D0':
			result += 1.0*b
		else:
			result += 0.0
	
print(round(result/s, 6))