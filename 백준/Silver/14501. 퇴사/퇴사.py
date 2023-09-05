import sys
input = sys.stdin.readline

def recur(day, result):
	global answer
	if N == day:
		answer = max(answer, result)
		return
	
	# 상담을 할 때, 상담을 하기 위해서 1. 상담이 끝나는 날이 퇴사 전이어야 함.
	if day + ingre[day][0] <= N:
		
		recur(day + ingre[day][0], result + ingre[day][1])
	
	# 상담을 하지 않을 때
	recur(day+1, result)

N = int(input())
ingre = [list(map(int, input().split())) for i in range(N)]

answer = 0

recur(0, 0)

print(answer)