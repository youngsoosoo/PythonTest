def solution(elements):
    l = len(elements)
    elements = elements*2
    result=set()
    for i in range(l):
        for j in range(l):
            result.add(sum(elements[j:j+i+1]))

    return len(result)