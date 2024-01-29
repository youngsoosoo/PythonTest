import sys
input = sys.stdin.readline

n = int(input())
koi = list(map(int, input().split()))
koi.sort()

left, right = 0, n-1

answer = abs(koi[left] + koi[right])
result = [koi[left], koi[right]]

while left < right:
	leftValue = koi[left]
	rightValue = koi[right]
	
	sumValue = leftValue + rightValue
	
	if abs(sumValue) < answer:
		answer = abs(sumValue)
		result = [leftValue, rightValue]
		if answer == 0:
			break
	
	if sumValue < 0:
		left += 1
	else:
		right -= 1
		
print(*result)