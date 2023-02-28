from collections import deque

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = deque(list(format(bin(arr1[i])[2:])))
        b = deque(list(format(bin(arr2[i])[2:])))
        arr=''
        for j in range(n):
            if len(a) == n:
                break
            a.appendleft('0')
        for j in range(n):
            if len(b) == n:
                break
            b.appendleft('0')
        for i in range(n):
            if a[i] == b[i] == '0':
                arr+=' '
            else:
                arr+='#'
        answer.append(arr)
            
    return answer