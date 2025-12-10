def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    li = []
    
    for city in cities:
        city = city.lower()
        n = len(li)
        if city not in li:
            answer += 5
            if n == cacheSize:
                li.pop(0)
        else:
            answer += 1
            li.remove(city)
        li.append(city)
                
    
    return answer