from itertools import permutations
def operation(a, b, c):
    if c == '*':
        result = int(a) * int(b)
    elif c == '-':
        result = int(a) - int(b)
    else:
        result = int(a) + int(b)
    return result

def calculate(exp,op):
    array=[]
    tmp=""
    
    for i in exp:
        if i.isdigit()==True:
            tmp+=i
        else:
            array.append(tmp)
            array.append(i)
            tmp=""
    array.append(tmp)
    
    for o in op:
        stack=[]
        while len(array)!=0:
            tmp=array.pop(0)
            if tmp==o:
                stack.append(operation(stack.pop(), array.pop(0), o))
            else:
                stack.append(tmp)
        array=stack
            
    return abs(int(array[0]))

def solution(expression):
    
    op = ['+', '-', '*']
    op = list(permutations(op, 3))
    result=[]
    for i in op:
        result.append(calculate(expression, i))
    return max(result)