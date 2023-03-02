def solution(id_list, report, k):
    answer = [0 for i in id_list]
    report = set(report)
    report = list(report)
    dic = {i:[] for i in id_list}
    graph = [set() for i in range(len(id_list))]
    for i in range(len(report)):
        report[i] = list(report[i].split())
        graph[id_list.index(report[i][0])].add(report[i][1])
        dic[report[i][1]].append(id_list.index(report[i][0]))
    
    for i in id_list:
        if len(dic[i]) > 1:
            for j in dic[i]:
                answer[j]+=1


    return answer