import sys
input = sys.stdin.readline

# 누적합, 이모스법
n, h = map(int, input().split())

# 1. 배열을 주어진 높이+1만큼 공간을 할당
wall = [0] * (h+1)

# 2. 주어진 길이만큼 반복문 실행
for i in range(n):
	
	a = int(input())
	
	# 3. i에 따라 장애물을 구분해준 뒤, 이모스 법을 따라 처음과 끝에 +1, -1을 합산
	if i % 2 == 0:
		wall[0] += 1
		wall[a+1] -= 1
	else:
		wall[h-a+1] += 1
		wall[h] -= 1

# 4. 합산한 값을 누적합
for i in range(1, h):
	wall[i] += wall[i-1]

# 5. 최소 값과 개수 산출.
m = min(wall[:-1])

print(m, wall[:-1].count(m))