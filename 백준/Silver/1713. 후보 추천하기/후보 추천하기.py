import sys
input = sys.stdin.readline

n = int(input())
count = int(input())

students = list(map(int, input().split()))

dic = dict()

idx_arr = []
val_arr = []

for student in students:
	if student in dic:
		dic[student] += 1
	else:
		if len(dic) >= n:
			for k in dic.keys():
				if dic[k] == min(dic.values()):
					del dic[k]
					break
		dic[student] = 1

print(*sorted(dic.keys()))