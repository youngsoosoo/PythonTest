def solution(enroll, referral, seller, amount):
    
    n = len(enroll)
    answer = [0 for i in range(n+1)]
    par = [i for i in range(n+1)]
    dic = dict()
    
    def _find(sell, idx):
        if par[idx] == idx or sell // 10 == 0:
            answer[idx] += sell
            return
        
        balance = sell//10
        answer[idx] += (sell - balance)
        _find(balance, par[idx])
        return
    
    for i in range(n):
        dic[enroll[i]] = i+1
        
    for i in range(n):
        if referral[i] == "-":
            par[i+1] = 0
        else:
            par[i+1] = dic[referral[i]]
    
    for i in range(len(seller)):
        sel = seller[i]
        amo = amount[i]*100
        _find(amo, dic[sel])
    
    return answer[1:]