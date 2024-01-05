import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
s = [i for i in range(1, N+1)]

for i in permutations(s, N):
	print(*i)