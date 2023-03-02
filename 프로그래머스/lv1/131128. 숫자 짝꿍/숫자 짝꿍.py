def solution(X, Y):
    answer = ''
    x = {str(i):X.count(str(i)) for i in range(10)}
    y = {str(i):Y.count(str(i)) for i in range(10)}
    
    for i in range(9, -1, -1):
        i = str(i)
        n = min(x[i], y[i])
        
        if answer == '' and i == '0' and n != 0:
            return "0"
        
        answer = ''.join([answer, i*n])  
    
    if answer=='':
        answer='-1'
    return str(answer)