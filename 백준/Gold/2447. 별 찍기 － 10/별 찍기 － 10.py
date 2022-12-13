import sys
input = sys.stdin.readline

def star(n):
	if n == 1:
		return['*']
	stars = star(n//3)
	arr = []
	for s in stars:
		arr.append(s*3)
	for s in stars:
		arr.append(s+' '*(n//3)+s)
	for s in stars:
		arr.append(s*3)
	
	return arr

n = int(input())
print('\n'.join(star(n)))