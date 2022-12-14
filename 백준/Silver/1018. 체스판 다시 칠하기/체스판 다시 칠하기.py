import sys
input = sys.stdin.readline
	
n, m = map(int,input().split())#세로, 가로
arr = [list(input().rstrip()) for i in range(n)]
result = []

#맨 위칸이 흰색이나 검은색 인 경우
for i in range(n-7):
	for j in range(m-7):
		a = 0
		b = 0
		for k in range(i, i+8):
			for l in range(j, j+8):
				if (k+l) % 2 == 0:
					if arr[k][l] != 'B':
						a += 1
					if arr[k][l] != 'W':
						b += 1
				else:
					if arr[k][l] != 'W':
						a += 1
					if arr[k][l] != 'B':
						b += 1
		result.append(a)
		result.append(b)
		
print(min(result))