import sys
input = sys.stdin.readline

n = int(input())
ti = list(map(int, input().split()))

ti.sort()

for i in range(1, n):
	ti[i] += ti[i-1]
print(sum(ti))