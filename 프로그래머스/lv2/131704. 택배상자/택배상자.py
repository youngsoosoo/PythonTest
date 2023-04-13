def solution(order):
    answer = 0
    stack = []
    l = len(order)
    i=1
    while i <= l:
        stack.append(i)
        while stack and stack[-1] == order[answer]:
            answer+=1
            stack.pop()
        
        i+=1
    return answer
