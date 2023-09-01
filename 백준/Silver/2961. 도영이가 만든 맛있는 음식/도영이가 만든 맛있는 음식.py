import sys
input = sys.stdin.readline

def recur(idx, dan, zzan, use):
	
	global answer
	
	if idx == n:
		if use == 0:
			return
		result = abs(dan - zzan)
		answer = min(answer, result)
		return
	
	recur(idx+1, dan + ingre[idx][1], zzan * ingre[idx][0], use + 1)
	
	recur(idx+1, dan, zzan, use)

n = int(input())
ingre = [list(map(int, input().split())) for _ in range(n)]

# 음식의 신맛은 사용한 재료의 신맛의 곱, 쓴맛은 합

answer = sys.maxsize

recur(0, 0, 1, 0)

print(answer)