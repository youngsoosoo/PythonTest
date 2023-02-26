def solution(k, score):
    answer = []
    arr=[]
    for i in score:
        if len(arr) == 0:
            arr.append(i)
            answer.append(i)
        elif len(arr) >= k:
            arr.sort(reverse=True)
            if arr[-1] < i:
                arr.pop()
                arr.append(i)
            answer.append(min(arr))
        else:
            arr.append(i)
            answer.append(min(arr))
        
    
    return answer