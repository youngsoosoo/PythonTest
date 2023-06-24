import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

left, right = 0, 0  # 슬라이딩 윈도우의 왼쪽과 오른쪽 인덱스
window_sum = 0  # 슬라이딩 윈도우 내의 합
result = sys.maxsize

while True:
	if window_sum >= s:
		result = min(result, right - left)  # 최소 길이 갱신
		window_sum -= arr[left]  # 슬라이딩 윈도우 왼쪽 값을 빼주고 왼쪽 인덱스 이동
		left += 1
	elif right == n:  # 오른쪽 인덱스가 끝에 도달하면 종료
		break
	else:
		window_sum += arr[right]  # 슬라이딩 윈도우 오른쪽 값을 더해주고 오른쪽 인덱스 이동
		right += 1
		
if result == sys.maxsize:
	print(0)
else:
	print(result)
