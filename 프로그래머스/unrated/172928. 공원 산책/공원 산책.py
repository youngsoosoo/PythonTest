### 문제 인식 ###
# 강아지가 지날 수 있는 길 O, 못 가는 길 X
# 주어진 명령을 수행하는데 이때 공원에 벗어나거나 장애물을 만나면 명령을 수행하지 않습니다.
### 문제 해결 방법 ###
# O(n^3)도 괜찮을듯.
# 1. 시작점을 구해줍니다.
# 2. 주어진 routes 를 통해 이동할 방향과 이동할 칸 수를 구해줍니다.
# 3. 이동할 방향과 이동할 칸 수를 통해 이동시켜줍니다. 이때, 중간에 장애물이 있거나 공원을 벗어나면 이동시키지 않습니다.
def solution(park, routes):
    
    H = len(park)
    W = len(park[0])
    
    # 1
    for i in range(H):
        for j in range(W):
            if park[i][j] == 'S':
                x = i
                y = j
                break

    # x가 세로 y가 가로
    for i in routes:
        # 2
        a, b = map(str, i.split())
        b = int(b)
        flag=1
        
        # 3
        if a == "N" and x-b >= 0:
            for i in range(x-b, x):
                if park[i][y] == "X":
                    flag = 0
                    break
            if flag:
                x-=b
                
        elif a == "S" and x+b <= H-1:
            for i in range(x, x+b+1):
                if park[i][y] == "X":
                    flag = 0
                    break
            if flag:
                x+=b
                
        elif a == "W" and y-b >= 0:
            for i in range(y-b, y):
                if park[x][i] == "X":
                    flag = 0
                    break
            if flag:
                y-=b
                
        elif a == "E" and y+b <= W-1:
            for i in range(y, y+b+1):
                if park[x][i] == "X":
                    flag = 0
                    break
            if flag:
                y+=b
    
    
    return [x,y]