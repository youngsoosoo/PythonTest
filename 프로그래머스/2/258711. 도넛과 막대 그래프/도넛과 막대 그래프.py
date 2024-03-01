# 하나도 거치지 않고 돌아오면 도넛 모양 그래프 [1?, 1?]
# 다시 돌아오지 않는다면 막대 모양 그래프 [나가는 간선의 수 0, 들어오는 간선의 수 1]
# 여러 개를 거쳐서 돌아온다면 8자 모양 그래프 [나가는 간선의 수 2, 들어오는 간선의 수 2]
# 들어오는 것은 없고 나가는 것만 있다면 정점 [2이상, 0]
# [나가는 것, 들어오는 것]
def solution(edges):
    answer = [0, 0, 0, 0]
    graph = dict()
    for a, b in edges:
        if a not in graph:
            graph[a] = [0, 0]
        if b not in graph:
            graph[b] = [0, 0]
        graph[a][0] += 1
        graph[b][1] += 1
    
    for k, v in graph.items():
        
        # 정점
        if v[0] > 1 and v[1] == 0 :
            answer[0] = k
        # 막대
        elif v[0] == 0 and v[1] > 0:
            answer[2] += 1
        # 8자
        elif v[0] > 1 and v[1] > 1:
            answer[3] += 1
    # 도넛
    answer[1] = graph[answer[0]][0] - answer[2] - answer[3]
    
    return answer