
def solution(priorities, location):
    answer = 0
    result=[]
    i=0
    while True:
        i = i%len(priorities)
        if priorities[i] == max(priorities):
            answer+=1
            priorities[i] = 0
            if i == location:
                break
        i+=1
        
    return answer