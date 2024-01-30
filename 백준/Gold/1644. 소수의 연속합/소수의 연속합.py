import sys
input = sys.stdin.readline

n = int(input())
answer = 0

prime = [True] * (n+1)
prime[0] = False
prime[1] = False

for i in range(2, (n**1//2)+1):
	if prime[i] == True:
		j = 2
		
		while i*j <= n:
			prime[i*j] = False
			j+=1

prime_number = [i for i in range(2, n+1) if prime[i] == True]

left = 0
right = 1
while right <= len(prime_number):
	sumValue = sum(prime_number[left:right])
	if sumValue == n:
		answer+=1
		right+=1
	elif sumValue < n:
		right+=1
	else:
		left+=1
		
print(answer)