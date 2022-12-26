import sys
input = sys.stdin.readline

maxnum = -1e9
minnum = 1e9
n = int(input())
a = list(map(int, input().split()))
op = list(map(int, input().split()))

def dfs(depth, total, pl, mi, mul, div):
	global maxnum, minnum
	if depth == n:
		maxnum = max(total, maxnum)
		minnum = min(total, minnum)
		return
	if pl:
		dfs(depth + 1, total + a[depth], pl - 1, mi, mul, div)
	if mi:
		dfs(depth + 1, total - a[depth], pl, mi-1, mul, div)
	if mul:
		dfs(depth + 1, total * a[depth], pl, mi, mul-1, div)
	if div:
		dfs(depth + 1, int(total / a[depth]), pl, mi, mul, div-1)

dfs(1, a[0], op[0], op[1], op[2], op[3])
print(maxnum)
print(minnum)