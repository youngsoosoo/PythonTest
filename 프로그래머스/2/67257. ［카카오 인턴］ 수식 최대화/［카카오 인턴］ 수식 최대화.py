from itertools import permutations
def operation(data, data1, data2):
    if data == '+':
        return str(data1 + data2)
    if data == '-':
        return str(data1 - data2)
    if data == '*':
        return str(data1 * data2)
    
def calculation(s_stack, per):
    
    for p in per:
        stack = []

        while s_stack:
            data = s_stack.pop(0)
                
            if data == p:
                data1 = stack.pop()
                data2 = s_stack.pop(0)
                stack.append(operation(data, int(data1), int(data2)))
            else:
                stack.append(data)
                    
        s_stack = stack
        
    return abs(int(s_stack[0]))
    

def solution(expression):
    answer = []
    
    for per in permutations(['*', '+', '-'], 3):
        
        s = ""
        s_stack = []
    
        for e in expression:
            if e.isdigit():
                s += e
            else:
                s_stack.append(s)
                s_stack.append(e)
                s=""
        s_stack.append(s)
        
        answer.append(calculation(s_stack, per))
    
    return max(answer)