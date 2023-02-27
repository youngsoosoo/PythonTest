def solution(x):
    answer = True
    x=str(x)
    a = list(x)
    b=0
    for i in a:
        b += int(i)
    if int(x)%b != 0:
        answer = False
    return answer