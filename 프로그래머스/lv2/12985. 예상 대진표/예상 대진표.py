def solution(n,a,b):
    answer = 0
    while True:
        answer+=1
        if a%2==1:
            a+=1
        a=a//2
        if b%2==1:
            b+=1
        b=b//2
        if a == b:
            break
        
    return answer