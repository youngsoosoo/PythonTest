# 브루트 포스
# 모든 것을 탐색하며 적어도 k개의 체커가 갈 수 있는 최소 횟수를 구한다

import sys
input = sys.stdin.readline

n = int(input())
checker = [list(map(int, input().split())) for _ in range(n)]

answer = [sys.maxsize] * n

l = len(checker)

for i in checker:
	for j in checker:
		x1, y1 = i[0], j[1]
		
		value = list()
		for x2, y2 in checker:
			value.append(abs(x2-x1) + abs(y2-y1))
		value.sort()
		
		s = 0
		for k in range(n):
			s += value[k]
			if answer[k] > s:
				answer[k] = s

print(*answer)