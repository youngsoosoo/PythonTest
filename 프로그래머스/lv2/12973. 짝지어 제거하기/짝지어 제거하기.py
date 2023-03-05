def solution(s):
    answer = 0
    arr=[]
    for i in s:
        arr.append(i)
        if len(arr) > 1 and arr[-1] == arr[-2]:
            arr.pop()
            arr.pop()
    if len(arr) == 0:
        answer=1
    return answer