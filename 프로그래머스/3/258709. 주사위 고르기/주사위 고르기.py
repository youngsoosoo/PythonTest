from itertools import combinations, product
def solution(dice):
    answer = []
    dic = dict()
    l = len(dice)
    
    for a in combinations(range(l), l//2):
        b = [i for i in range(l) if i not in a]
        
        aList = []
        bList = []
        for c in product(range(6), repeat=l//2):
            aList.append(sum(dice[i][j] for i, j in zip(a, c)))
            bList.append(sum(dice[i][j] for i, j in zip(b, c)))
            
        bList.sort()
        
        a_win=0
        b_win=0
        
        for num in aList:
            start=0
            end=len(bList)
            
            while start<end:
                mid = (start+end)//2
                
                if bList[mid] >= num:
                    end = mid
                else:
                    start = mid+1
            
            a_win += start
        dic[a_win] = list(a)
    
    return [i+1 for i in dic[max(dic.keys())]]