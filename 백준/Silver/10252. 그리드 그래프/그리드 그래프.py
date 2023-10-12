import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
	m, n = map(int, input().split())
	i, j = 0, 0
	print("1")
	while True:
		print(f"({i},{j})")
		if i % 2:
			j -= 1
		else:
			j += 1
		if j >= n or j < 1:
			i += 1
			if i % 2:
				j -= 1
			else:
				j += 1
		if i == m:
			break
	for i in range(m - 1, 0, -1):
		print(f"({i},0)")