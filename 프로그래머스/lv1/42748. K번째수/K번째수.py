def solution(array, commands):
    answer = []
    for a in commands:
        i, j ,k = a[0], a[1], a[2]
        arr = array[i-1:j]
        arr.sort()
        answer.append(arr[k-1])
    return answer