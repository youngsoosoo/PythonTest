def solution(s):
    answer = ''
    a=0
    for i in s:
        if a % 2 == 0 :
            answer+=i.upper()
        else:
            answer+=i.lower()
        a+=1
        if i == " ":
            a=0
    return answer