import sys
import itertools
input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort(reverse=True)
le = len(str(n))

while True:
	a = list(itertools.product(arr,repeat=le))

	result = []
	for i in a:
		temp = int(''.join(i))
		if n >= temp:
			result.append(temp)
	if len(result) >=1:
		print(max(result))
		break
	else:
		le-=1
