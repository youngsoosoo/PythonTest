import sys
input = sys.stdin.readline

def convert_to_base(num, base):
	convert_string = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/"
	if num < base:
		return convert_string[num]
	else:
		return convert_to_base(num//base, base) + convert_string[num%base]


t = int(input())
for _ in range(t):
	s = input()
	if s == s[::-1]:
		print(1)
	else:
		flag = 0
		for base in range(2, 65):
			a = convert_to_base(int(s), base)
			if a == a[::-1]:
				flag=1
		if flag:
			print(1)
		else:
			print(0)