import sys
import math
A, B, V = map(int, input().split())

cnt = (V-B) / (A-B)
print(math.ceil(cnt))