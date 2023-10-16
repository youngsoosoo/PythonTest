import sys
input = sys.stdin.readline

n = int(input())
qindex=sorted(list(map(int, input().split())))

for i in range(n, -1, -1):
	if i <= qindex[-i]:
		print(i)
		break