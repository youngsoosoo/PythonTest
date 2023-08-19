# 1. 갭을 줄여도 된다.
# 8 12
# 4 8

# 2. 최대 공약수라는 두 수 중 하나로 나누어서 나머지가 생기지 않는다.
# 8 12
# 최대 공약수

# 3. 한 수를 가능한 만큼 갭을 줄인다.
# 하나의 수를 작은 수로 되는 만큼 뺀다는 말은 나누고 나서 나머지를 뜻한다.

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

def _gcd(a, b):
	while b > 0:
		a, b = b, a % b# 나머지가 0이 되는 순간 멈춘다.
	return a

div = b // a
c, d = 1, div

for i in range(1, div//2+1):
	if div % i == 0:
		e = i
		f = div//i
		if _gcd(e, f) != 1:
			continue
		if c+d > e+f:
			c = e
			d = f
print(a * c, a * d)