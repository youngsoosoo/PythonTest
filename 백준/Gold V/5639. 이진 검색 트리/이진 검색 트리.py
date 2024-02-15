import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

arr = []
while True:
	try:
		x = int(input())
		arr.append(x)
	except:
		break

def tree(a):
	if len(a) == 0:
		return
	
	left, right = [], []
	mid = a[0]
	
	for i in range(1, len(a)):
		if a[i] > mid:
			left = a[1:i]
			right = a[i:]
			break
	else:
		left = a[1:]
	
	tree(left)
	tree(right)
	print(mid)
	
tree(arr)