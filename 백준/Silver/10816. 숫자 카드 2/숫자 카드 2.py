import sys
input = sys.stdin.readline

n = int(input())
arr = map(int, input().split())
m = int(input())
hashmap={}

for i in arr :
	if i in hashmap:
		hashmap[i] += 1
	else:
		hashmap[i] = 1
	
print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in map(int, input().split())), end=" ")