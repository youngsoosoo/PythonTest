import sys
input = sys.stdin.readline

n = int(input())
meet = [list(map(int, input().split())) for _ in range(n)]
meet.sort(key=lambda x :(x[1], x[0]))
a=meet[0][1]
cnt=1
for i in range(1, n):
	if a <= meet[i][0]:
		a=meet[i][1]
		cnt+=1
print(cnt)