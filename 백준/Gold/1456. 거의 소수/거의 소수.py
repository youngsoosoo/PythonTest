import sys
input = sys.stdin.readline

a, b = map(int, input().split())
answer = 0
prime = [True] * (int(b**0.5) + 1)
prime[1] = False

for i in range(2, int(b**0.5) + 1):
	if prime[i]:
		if i*i>int(b**0.5):
			break
		for j in range(i*2, int(b**0.5) + 1, i):
			prime[j] = False
		
for i in range(2, len(prime)):
	if prime[i]:
		n = i*i
		while n <= b:
			if n < a:
				n*=i
				continue
			answer+=1
			n*=i

print(answer)