### 문제 인식 ###
# 선공은 O로, 후공은 X로 틱택토 게임을 진행합니다.
# 3*3의 게임판으로 되어있고, 가로/세로/대각선으로 3개가 같은 표시라면
# 게임이 종료되고 먼저 만든 사람이 승리하게 됩니다.
# 주어진 조건을 지켜 정상적인 게임일 때 1을 비정상적인 게임일 때 0을 return 하면 됩니다.
### 문제 해결 ###
# 1. X의 개수가 더 많다면 0
# 2. 한쪽이 가로/세로/대각선으로 3개를 먼저 점령했는데 다른 것도 3개라면 0
# 3. X가 3개라 끝났지만 O는 4개일 때(게임이 종료되어야 하는데 이후 지속)
# 4. O가 3개라 끝났지만 X의 개수가 O와 같을 때(게임이 종료되어야 하는데 이후 지속)
# 위의 4개의 조건이 해당된다면 0을 return 합니다.
# 먼저 반복문을 통해 모든 것을 돌면서 가로/세로/대각선을 모두 확인해봅니다.
# 정상적이라면 1을 리턴해 게임을 종료합니다.

from collections import Counter

# 게임 정상 종료 여부
def gameStart(board, colboard, cnt):
    
    resultO = 0
    resultX = 0

    # 가로
    for i in range(3):
        if Counter(board[i])['O'] == 3 or Counter(colboard[i])['O'] == 3:
            resultO = 1
        if Counter(board[i])['X'] == 3 or Counter(colboard[i])['X'] == 3:
            resultX = 1

    # 대각선
    for i in range(0, 3, 2):
        print(i)
        if board[0][i] == board[1][1] == board[2][2-i] == 'O':
            resultO = 1
        if board[0][i] == board[1][1] == board[2][2-i] == 'X':
            resultX = 1
    # 1. O와 X가 모두 3개일 때
    # 2. X가 3개라 끝났지만 O는 4개일 때(게임이 종료되어야 하는데 이후 지속)
    # 3. O가 3개라 끝났지만 X의 개수가 O와 같을 때(게임이 종료되어야 하는데 이후 지속)
    if resultO and resultX or resultX and cnt or resultO and not cnt:
        return 0
    return 1

def solution(board):
    
    sb = ''.join(board)
    cnt = sb.count('O') - sb.count('X')
    if cnt not in [0, 1]:
        return 0
    
    colboard = list(zip(*board))
    
    return gameStart(board, colboard, cnt)
