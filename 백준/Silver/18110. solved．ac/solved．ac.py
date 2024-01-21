import sys
input = sys.stdin.readline

def my_round(val):
	return int(val) + 1 if val - int(val) >= 0.5 else int(val)

n = int(input())
if n:
	arr = sorted([int(input()) for _ in range(n)])
	result = my_round(n * 0.15)
	print(my_round(sum(arr[result:-result] if result else arr) / (n - 2 * result)))
else:
	print(0)