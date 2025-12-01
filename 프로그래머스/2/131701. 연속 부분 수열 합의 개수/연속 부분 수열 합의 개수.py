def solution(elements):
    
    setList = set()
    
    for i in range(len(elements)):
        answer = elements[i]
        setList.add(answer)
        for j in range(i+1, i + len(elements)):
            answer += elements[j%len(elements)]
            setList.add(answer)
    
    return len(setList)