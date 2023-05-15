### 문제 인식 ###
# 1번부터 시작해 상자 안에 있는 숫자의 상자로 넘어간다.
# 이때 상자가 더이상 이어지지 않는다면 지금까지 지나온 상자는 i번 상자 그룹에 포함된다.
# 1번 상자 그룹만 있다면 점수는 0점으로 종료됩니다.
# 이렇게 여러 개의 상자 그룹이 생겼을 때 두 개의 상자를 골라 곱해 최고점수를 리턴하면 됩니다.
### 문제 해결 ###
# dfs를 사용하여 각 상자 그룹의 길이를 answer 배열에 추가해줍니다.
# 그 중 가장 큰 값 두 개를 골라 곱한 값을 출력해줍니다.

def solution(cards):
    answer = []
    l = len(cards)
    visited = [0 for _ in range(l)]

    for i in range(l):
        if not visited[i]:
            cnt = 0
            
            while True:
                if visited[cards[i]-1] == 0:
                    visited[cards[i]-1] = 1
                    cnt += 1
                    i = cards[i]-1
                else:
                    break
            answer.append(cnt)

    if len(answer) == 1:
        return 0
    else:
        answer.sort(reverse=True)

    return answer[0] * answer[1]
