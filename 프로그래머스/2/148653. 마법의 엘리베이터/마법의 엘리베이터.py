def solution(storey):
    answer = 0
    
    while storey:
        s = storey%10
        
        if s == 5:
            if (storey//10)%10 >= 5:
                storey+=10
            answer += s
        elif s < 5:
            answer += s
        else:
            answer += (10-s)
            storey += 10
        storey //= 10
        
    return answer