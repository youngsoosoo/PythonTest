def solution(answers):
    answer = []
    visited=[0 for i in range(4)]
    graph = [[],
          [1, 2, 3, 4, 5],
          [2, 1, 2, 3, 2, 4, 2, 5],
          [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
         ]
    for i in range(len(answers)):
        for j in range(1, len(graph)):
            if answers[i] == graph[j][i%len(graph[j])]:
                visited[j]+=1
    a = max(visited)
    for i in range(1, len(visited)):
        if a == visited[i]:
            answer.append(i)
    return answer