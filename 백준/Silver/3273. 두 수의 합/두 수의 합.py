import sys
input = sys.stdin.readline

# 9
# 5 12 7 10 9 1 2 3 11
# 13

n = int(input())
arr = list(map(int, input().split()))
x = int(input())
answer = 0
arr.sort()

start = 0
end = n-1

while start < end:
	
	# x와 같을 때
	if arr[start] + arr[end] == x:
		answer += 1
		start+=1
		end -= 1
	# x보다 작을 때
	elif arr[start] + arr[end] < x:
		start += 1
	# x보다 클 때
	else:
		end -= 1

print(answer)