### 문제 인식 ###
# 자연수 n에 대해 3가지의 작업을 반복하면 항상 1로 만들 수 있습니다.
# 주어지는 구간에 대한 우박수열 정적분을 구하려고 합니다.
# 주어지는 구간에 대한 우박수열 정적분은 주어진 구간의 넓이와 같습니다.
### 문제 해결 ###
# 먼저 필요한 좌표를 가지고 우박수열 정적분을 구하기 위한 구간의 넓이를 구해줍니다.
# 주어진 구간에 대해 넓이를 구하고 답을 도출합니다.
def solution(k, ranges):
    answer = []
    cnt = 0
    graph = []
    result = []
    while True:
        graph.append((cnt, k))
        print(cnt, k)
        if cnt > 0:
            # 3개의 변에 대한 길이를 구합니다.
            # x = 가로길이
            # y_1은 이전 구간에 대한 높이
            # y_2는 현재 구간의 높이와 이전 구간의 높이를 뺀 수
            x = graph[cnt][0] - graph[cnt-1][0]
            y_1 = graph[cnt-1][1]
            y_2 = graph[cnt][1] - graph[cnt-1][1]
            
            # 구간의 크기를 계산해줍니다.
            result.append(x*y_1 + x*y_2/2)
        if k == 1:
            break
        if k%2 == 0:
            k = k//2
        else:
            k = k*3 + 1
        
        cnt+=1
    
    for x, y in ranges:
        if x > y+cnt:
            answer.append(-1)
        else:
            answer.append(sum(result[x:cnt + y]))
    
    return answer