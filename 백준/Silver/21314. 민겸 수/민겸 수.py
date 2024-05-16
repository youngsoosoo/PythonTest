import sys
input = sys.stdin.readline

s = input().rstrip()

min_answer = ""
m_stack = 0
# 최솟값
for i in s:
	if i == "K":
		if m_stack > 0:
			min_answer += str(10 ** (m_stack-1))
			m_stack = 0
		min_answer += "5"
	else:
		m_stack += 1
if m_stack > 0:
	min_answer += str(10 ** (m_stack-1))
	m_stack = 0

max_answer = ""
# 최댓값
for i in s:
	if i == "K":
		if m_stack > 0:
			max_answer += str(5 * (10 ** m_stack))
			m_stack = 0
		elif m_stack == 0:
			max_answer += "5"
	else:
		m_stack += 1

if m_stack > 0:
	if i == "K":
		max_answer += str(5 * (10 ** m_stack))
	else:
		max_answer += str("1" * m_stack)

print(max_answer)
print(min_answer)
	