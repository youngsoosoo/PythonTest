import sys
input = sys.stdin.readline

def recur(idx, A, B, C, D, E, arr):
	global answer, result, n
	if idx == n:
		if a <= A and b <= B and c <= C and d <= D: # 모든 필요 영양소를 충족했다면
			if answer > E:
				answer = E
				result = arr
	else:
		if sum(ingre[idx][:-1]) > 0 and (a > A or b > B or c > C or d > D):
			# 재료를 사용한 경우에는 영양소가 더해진다.
			recur(idx+1, A + ingre[idx][0], B + ingre[idx][1], C + ingre[idx][2], D + ingre[idx][3], E + ingre[idx][4], arr + [idx+1])
		# 재료를 사용하지 않은 경우에는 그냥 다음 재료로 넘어간다.
		recur(idx+1, A, B, C, D, E, arr)

n = int(input())
# 최소 영양 성분, 단백질, 지방, 탄수화물, 비타민
a, b, c, d = map(int, input().split())

# 단백질, 지방, 탄수화물, 비타민, 가격
ingre = [list(map(int, input().split())) for i in range(n)]

answer = sys.maxsize
result = []
recur(0, 0, 0, 0, 0, 0, [])

if answer == sys.maxsize:
	print(-1)
else:
	print(answer)
	print(*result)