def solution(s):
    answer = [0, 0]
    while True:
        if s == '1':
            break
        answer[1]+=s.count('0')
        s = s.replace('0', '')
        s = bin(len(s))[2:]
        answer[0]+=1
    
    return answer