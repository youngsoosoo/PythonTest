def solution(msg):
    answer = []
    d = {chr(i) : i-64 for i in range(65,91)} # 사전
    idx = 27 # 사전 색인 번호
    start, end = 0, 1 # 단어 인덱스 시작, 끝
    while end < len(msg)+1:
        s = msg[start:end]
        if s in d:
            end+=1
        else:
            answer.append(d[s[:-1]])
            d[s] = idx
            idx+=1
            start = end-1
    answer.append(d[s])
            
    return answer