import sys
input = sys.stdin.readline

n = int(input())
answer = 1

n = (n + 1) // 2

for i in range(n):
    answer = (answer * 2) % 16769023

print(answer)