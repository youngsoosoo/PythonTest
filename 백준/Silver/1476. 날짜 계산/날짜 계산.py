import sys
input = sys.stdin.readline

E, S, M = map(int ,input().split())

cnt = 1
while True:
	
	if (cnt-E) % 15 == 0 and (cnt-S) % 28 == 0 and (cnt-M) % 19 == 0:
		print(cnt)
		break
	
	cnt+=1