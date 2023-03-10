def convert(n, q) :
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += str(mod)

    return rev_base[::-1] 

def primenumber(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5)+1):	# 2부터 x-1까지의 모든 숫자
    	if x % i == 0:		# 나눠떨어지는게 하나라도 있으면 False
        	return False
    return True	

def solution(n, k):
    answer = 0
    s=''
    for i in convert(n, k):
        if i == '0' and len(s) != 0:
            print(s)
            if int(s) > 1 and primenumber(int(s)):
                answer+=1
            s = ''
        else:
            s+=i
    if int(s) > 1 and primenumber(int(s)):
        answer+=1
    return answer