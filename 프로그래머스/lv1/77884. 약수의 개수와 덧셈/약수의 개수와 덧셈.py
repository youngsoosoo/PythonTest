def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        cnt=0
        for j in range(1, int(i**(1/2))+1):
            if i%j == 0:
                if j == i//j:
                    cnt+=1
                else:
                    cnt+=2
        if cnt % 2 ==0:
            answer+=i
        else:
            answer-=i
    return answer