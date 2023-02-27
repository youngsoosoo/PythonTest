def solution(arr):
    answer = arr
    answer.remove(min(answer))
    if len(answer) == 0:
        answer.append(-1)
    return answer