from itertools import combinations
def solution(info, query):
    answer = []
    dic = dict()
    # 모든 경우의 수
    for i in info:
        i = i.split()
        for j in range(5):
            for c in combinations(i[:-1], j):
                _key = "".join(c)
                if _key in dic:
                    dic[_key].append(int(i[-1]))
                else:
                    dic[_key] = [int(i[-1])]
    
    for i in dic:
        dic[i].sort()
    
    def lower_bound(begin, end, target_list, target):
        if begin >= end:
            return begin    
        mid = (begin + end) // 2
        if target_list[mid] >= target:
            return lower_bound(begin, mid, target_list, target)
        else:
            return lower_bound(mid+1, end, target_list, target)
    
    for q in query:
        q = q.replace("and ", "")
        q = q.split()
        score = q[-1]
        
        _key = "".join(q[:4]).replace("-", "")
        cnt = 0
        if _key in dic:
            dic_score = dic[_key]
            
            if dic_score:
                cnt = len(dic_score) - lower_bound(0, len(dic_score), dic_score, int(score))
        answer.append(cnt)
        
    return answer