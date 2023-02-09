import sys
input = sys.stdin.readline

n = int(input())
aa = list(map(int, input().split()))
result = [0]

for a in aa:
	if result[-1] < a:
		result.append(a)
	else:
		start, end = 1, len(result)
		while start < end:
			mid = (start+end)//2
			
			if result[mid] < a:
				start = mid+1
			else:
				end = mid
		result[end] = a
print(len(result)-1)