import sys
input = sys.stdin.readline

xp=[]
yp=[]
for i in range(3):
	x, y = map(int, input().split())
	xp.append(x)
	yp.append(y)

for i in range(3):
	if xp.count(xp[i]) == 1:
		x4 = xp[i]
	if yp.count(yp[i]) == 1:
		y4 = yp[i]
	
print(x4, y4)