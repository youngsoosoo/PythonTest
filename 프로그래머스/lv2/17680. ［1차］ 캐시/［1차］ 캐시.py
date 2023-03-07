def solution(cacheSize, cities):
    answer = 0
    cache = []
    idx=0
    if cacheSize == 0:
        return len(cities) * 5
    
    for i in cities:
        i=i.upper()
        if i in cache:
            cache.remove(i)
            cache.append(i)
            answer+=1
        else:
            answer+=5
            if idx < cacheSize:
                cache.append(i)
                idx += 1
            else:
                cache.pop(0)
                cache.append(i)
            
    return answer