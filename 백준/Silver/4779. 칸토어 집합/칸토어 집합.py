def cut(a,n): # a = 시작점
    if n == 1:
        return
    for i in range(a + n//3, a +(n//3)*2): # 가운데 문자열을 공백으로
        result[i] = ' '
    cut(a, n//3) # 왼쪽
    cut(a + n//3 * 2, n//3) # 오른쪽

import sys
input = sys.stdin.readline

while True:
    
    try :
        N = int(input())
        result = ['-']*(3**N) # 최초 리스트 집합
        cut(0, 3**N) # 자르기
        print(''.join(result))
    except : # EOF 발생
        break