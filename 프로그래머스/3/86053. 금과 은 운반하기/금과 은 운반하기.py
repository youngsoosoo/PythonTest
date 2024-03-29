def solution(a, b, g, s, w, t):
    answer = (10**5) * 2 * (10**9) * 2
    
    start = 0
    end = (10**5) * 2 * (10**9) * 2
    
    while start <= end:
        mid = (start + end) // 2
        gold = 0
        silver = 0
        sum_gs = 0
        
        for i in range(len(g)):
            _gold, _silver, _weight, _time = g[i], s[i], w[i], t[i]
            # 물건 운반 횟수
            cnt = mid // (_time*2)
            
            # 편도 한 번 더 갈 수 있을 때
            if mid % (_time*2) >= _time:
                cnt += 1
            
            gold += _gold if _gold < cnt * _weight else cnt * _weight
            silver += _silver if _silver < cnt * _weight else cnt * _weight
            sum_gs += _gold + _silver if _gold + _silver < cnt * _weight else cnt * _weight
            
        if a <= gold and b <= silver and a+b <= sum_gs:
            end = mid - 1
            answer = min(answer, mid)
        else:
            start = mid + 1
    
    
    return answer