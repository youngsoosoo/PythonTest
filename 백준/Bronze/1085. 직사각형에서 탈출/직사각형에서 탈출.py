import sys
input=sys.stdin.readline

x, y, w, h = map(int, input().split())

if (w-x) > (h-y) and x > y:
	if (h-y) > y :
		print(y)
	else:
		print(h-y)
elif (w-x) > (h-y) : #x<y
	if (h-y) > x:
		print(x)
	else:
		print(h-y)
elif x > y : 
	if (w-x) > y:
		print(y)
	else : 
		print(w-x)
else : 
	if (w-x) > x :
		print(x)
	else :	
		print(w-x)