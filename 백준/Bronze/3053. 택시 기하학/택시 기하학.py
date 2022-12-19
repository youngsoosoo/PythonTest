import sys
import math
input = sys.stdin.readline

r=int(input())

ban = round(r**2*math.pi, 6)

print(format(ban, ".6f"))
print(format(2*r*r, ".6f"))