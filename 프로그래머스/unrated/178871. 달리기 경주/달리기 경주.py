### 문제 인식 ###
# 경주가 끝났을 때 선수들의 이름을 1등부터 순서대로 배열에 담아 return
### 문제 해결 방법 ###
# 시간복잡도를 O(N^2) 미만으로 풀어야 합니다.
# 1. 모든 선수의 이름과 등번호를 dict의 형태로 정리해줍니다. player1 : 선수의 등번호, player2 : 선수의 이름
# 2. 이름을 불린 선수를 한 자리 앞의 선수와 자리를 바꿔줍니다. 이때, 이름과 등번호를 모두 바꿔줍니다.
def solution(players, callings):
    
    player1 = dict()
    player2 = dict()
    
    # 1 player1은 이름 : 등번호, player2는 등번호 : 이름
    for i in range(len(players)):
        player1[players[i]] = i
        player2[i] = players[i]
        
    
    # 2 i를 추월시켜주려면 먼저 앞 자리 사람의이름과 등번호를 알아내야함
    for i in callings:
        # i 는 선수의 이름
        # 선수의 등번호
        idx = player1[i]
        
        # 앞 선수의 이름 : name 등번호 : idx -1
        name = player2[idx-1]
        
        player1[i] = idx-1
        player2[idx-1] = i
        
        player1[name] = idx
        player2[idx] = name
        
    
        
    return list(player2.values())