import sys, math
input = sys.stdin.readline

n = [int(input()) for _ in range(int(input()))]
# 모든 수의 최대 공약수 구하기
for i in range(1, len(n)):
   if i == 1:
      a=abs(n[1]-n[0])
   else:
      a = math.gcd(abs(n[i] - n[i-1]), a)
d = list()
d.append(a)
for i in range(2, int(a**0.5)+1):
   if a%i == 0:
      d.append(i)
      if i!=a//i:
         d.append(a//i)
d.sort()
print(*d)