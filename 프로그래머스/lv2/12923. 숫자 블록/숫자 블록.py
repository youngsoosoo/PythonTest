### 문제 인식 ###
# 블록은 n*2, n*3, n*4, ... 순으로 설치합니다.
# 블록은 길이가 1억이고, 한 줄에 10칸이 존재합니다.
### 문제 해결 ###
# 모든 수를 돌아 입력하니 시간초과가 났습니다.
# 최대 약수를 구해서 넣어주면 시간을 더 단축시킬 수 있을 거 같습니다.
def solution(begin, end):
    answer = []
    
    for i in range(begin, end + 1):
        min_num = 1
        max_num = 1
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                if i // j <= 10000000:
                    min_num = j
                    answer.append(i // j)
                    break
                else:
                    max_num = j
        if i == 1:
            answer.append(0)
        elif min_num == 1:
            answer.append(max_num)
            
    return answer