import sys
input = sys.stdin.readline

A, B= map(int, input().split())
A-=1

def div(a):
	tmp = a
	for i in range(1, 99):
		# 두 수의 2의 개수를 2의 제곱 수들을 통해 구해주는 식
		# 여기서 i는 n 제곱을 뜻함
		tmp += (a//(2**i))*((2**i)-(2**(i-1)))
	return tmp

print(div(B) - div(A))