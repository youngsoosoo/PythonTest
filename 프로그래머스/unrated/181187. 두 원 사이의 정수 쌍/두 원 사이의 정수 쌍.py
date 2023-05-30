### 문제 인식 ###
# r1, r2라는 반지름을 가진 원들 사이의 점의 개수를 구해라
# 단, 점의 좌표는 정수
### 문제 해결 ###
# r1부터 r2까지 사이의 점의 개수를 구할 때
# 점의 개수에 관한 공식을 찾아서 대입해주면 될 거 같습니다.

import math

def solution(r1, r2):
    answer = 0  
    
    for i in range(1, r2 + 1):
        high_r1 = math.sqrt(r2 ** 2 - i ** 2)
        high_r2 = 0 if i > r1 else math.sqrt(r1 ** 2 - i ** 2)
        
        answer += math.floor(high_r1) - math.ceil(high_r2) + 1
          
    return answer * 4
