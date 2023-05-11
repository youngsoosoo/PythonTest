### 문제 설명 ###
# 문자열을 압축시켜야 합니다. 예를 들어 aaa= 3a
# 3개의 단위로도 압축이 가능하고 n개의 단위로도 압축이 가능합니다. 예를 들어 abcabc = 2abc

### 문제 해결 ###
# len(s)//2의 단위부터 1개 단위로 나누기 위해 반복문을 통해 구해줍니다.
# 반복문을 통해 temp와 같은 문자열이 존재하는지 탐색하고
# 있다면 카운트를 해주고
# 없다면 temp를 다음 문자열로 변경해주면서 새로운 문자열에 저장해줍니다.
# 모든 경우가 종료한 이후에 남은 temp의 문자열과 cnt 개수를 생각해
# 마지막 남은 문자열을 붙여줍니다.
# 이 과정을 len(s)//2의 단위부터 1개 단위까지 계산하고 answer에 가장 압축이 많이 된
# 문자열의 길이를 구해줍니다.

def solution(s):
    answer = 1001
    l = len(s)
    
    if l == 1:
        return 1
    
    # 압축 시켜줄 문자열의 단위를 구함.
    for i in range(1, (len(s) // 2)+1):
        temp = s[:i]
        cnt = 1
        index = ''
        
        # 반복문을 통해 temp와 같은 문자열이 존재하는지 탐색
        for j in range(i, l, i):
            if temp == s[j:i+j]:
                cnt += 1
            else:
                # temp와 같은 문자열의 개수를 구해 하나도 없었다면 그냥 temp를 붙이고
                if cnt == 1:
                    index += temp
                # temp와 같은 문자열이 있었다면 temp에 숫자를 붙임
                else:
                    index += str(cnt) + temp
                temp = s[j:i+j]
                cnt = 1
            
        # 마지막으로 남은 index를 붙여줍니다.
        if cnt == 1:
            index += temp
        
        else:
            index += str(cnt) + temp
        answer = min(answer, len(index))
    return answer