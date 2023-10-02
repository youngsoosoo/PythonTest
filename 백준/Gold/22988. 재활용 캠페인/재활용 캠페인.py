import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = sorted(list(map(int, input().split())))
	
start = 0
end = n-1

remain = 0
cnt = 0
while start <= end:
	
	if arr[end] == x:
		cnt += 1
		end -= 1
		continue
	
	if start == end:
		remain += 1
		break
	
	if arr[end] + arr[start] >= x/2:
		cnt += 1
		start += 1
		end -= 1
		
	else:
		start += 1
		remain += 1

print(cnt + remain//3)