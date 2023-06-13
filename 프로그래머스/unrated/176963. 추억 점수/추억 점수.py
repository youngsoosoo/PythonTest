### 문제 인식 ###
# 주어진 이름에 매겨진 그리움 점수가 있습니다.
# 주어진 photo에 대해 점수를 종합하고 결과를 출력
### 문제 해결 방법 ###
# O(N^3)
# 1. photo 안에 각 배열의 그리움 점수를 종합해 출력하는 과정입니다.
# 2. name의 길이와 yearning의 길이가 같으므로 길이를 통해 해당 문자가 안에 들어 있는지 확인하고
# 계산을 해줍니다.
def solution(name, yearning, photo):
    answer = []
    
    # 1
    for i in photo:
        # 2
        cnt = 0
        for j in range(len(name)):
            if name[j] in i:
                cnt+=yearning[j]
        answer.append(cnt)
    return answer