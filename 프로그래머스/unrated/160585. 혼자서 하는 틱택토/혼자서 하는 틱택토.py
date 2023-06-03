### 문제 인식 ###
# 선공은 O로, 후공은 X로 틱택토 게임을 진행합니다.
# 3*3의 게임판으로 되어있고, 가로/세로/대각선으로 3개가 같은 표시라면
# 게임이 종료되고 먼저 만든 사람이 승리하게 됩니다.
# 주어진 조건을 지켜 정상적인 게임일 때 1을 비정상적인 게임일 때 0을 return 하면 됩니다.
### 문제 해결 ###
# 1. X의 개수가 더 많다면 0
# 2. 한쪽이 가로/세로/대각선으로 3개를 먼저 점령했는데 다른 것도 3개라면 0
# 먼저 반복문을 통해 모든 것을 돌면서 가로/세로/대각선을 모두 확인해봅니다.
# 모든 곳을 순회할 때 X와O의 개수도 세어줍니다.
# 모든 과정이 종료되었을 때 조건에 맞지 않는 것이 존재한다면 0을 리턴해줍니다.
# 정상적이라면 1을 리턴해 게임을 종료합니다.

from collections import Counter

# 게임 정상 종료 여부
def gameStart(board, colboard, cnt):
    
    resultO = 0
    resultX = 0

    # 가로
    for i in range(3):
        if Counter(board[i])['O'] == 3 or Counter(colboard[i])['O'] == 3:
            resultO += 1
        if Counter(board[i])['X'] == 3 or Counter(colboard[i])['X'] == 3:
            resultX += 1

    # 대각선
    for i in range(0, 3, 2):
        if board[0][i] == board[1][1] == board[2][2-i] == 'O':
            resultO += 1
        if board[0][i] == board[1][1] == board[2][2-i] == 'X':
            resultX += 1
    
    if resultO and resultX or resultX and cnt or resultO and not cnt:
        return 0
    return 1

def solution(board):
    
    sb = ''.join(board)
    cnt = sb.count('O') - sb.count('X')
    if cnt not in [0, 1]:
        return 0
    
    colboard = list(zip(*board))
    
    answer = gameStart(board, colboard, cnt)
    print(answer)
    dic = {'O':0, 'X':0}
    for x in range(3):
        for y in range(3):
            if board[x][y] != '.':
                dic[board[x][y]] += 1
    
    if dic['X'] > dic['O'] or (dic['O'] - dic['X'] not in [0, 1]):
        answer = 0
    
    return answer