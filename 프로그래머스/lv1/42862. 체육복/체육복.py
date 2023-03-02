def solution(n, lost, reserve):
    answer = 0
    arr = [0]*(n+1)
    
    for i in lost:
        arr[i] -= 1
    for i in reserve:
        arr[i] += 1
    for i in range(1, n):
        if arr[i] == -1 and arr[i-1] == 1:
            arr[i] = 0
            arr[i-1] = 0
        elif arr[i] == -1 and arr[i+1] == 1:
            arr[i] = 0
            arr[i+1] = 0
    if arr[i+1] == -1 and arr[i] == 1:
        arr[i] = 0
        arr[i+1] = 0
    
    answer = arr.count(0)+arr.count(1)-1
    return answer