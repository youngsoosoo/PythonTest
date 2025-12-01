def solution(elements):
    
    setList = set()
    newElements = elements * 2
    
    for i in range(1, len(elements)+1):
        for j in range(1, len(elements)+1):
            setList.add(sum(newElements[i:i+j]))
    
    return len(setList)