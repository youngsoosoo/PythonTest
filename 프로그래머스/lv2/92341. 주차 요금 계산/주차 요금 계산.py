import math

def solution(fees, records):
    answer = []
    dic = dict()

    for i in records:
        time, number, history = i.split()
        number = int(number)
        time, minutes = map(int, time.split(':'))
        minutes +=time*60
        if number in dic:
            dic[number].append([minutes, history])
        else:
            dic[number] = [[minutes, history]]
    
    result = list(dic.items())
    result.sort(key=lambda x : x[0])
    
    for i in range(len(result)):
        money=0
        
        for j in result[i][1]:
            if j[1] == 'IN':
                money-=j[0]
            else:
                money+=j[0]

        if result[i][1][-1][1] == "IN":
            money += 23*60 + 59

        if money <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] +  math.ceil((money-fees[0])/fees[2])*fees[3])
    return answer