def solution(number, k):
    stack = []
    for i in range(len(number)):
        while stack and stack[-1] < number[i] and k > 0:
            stack.pop()
            k -= 1
        stack.append(number[i])
        if k == 0:
            stack += number[i+1:]
            break
    answer = ''.join(stack[:len(number)-k])
    return answer