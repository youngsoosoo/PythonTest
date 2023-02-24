def solution(s):
    answer = []
    result = {}
    for i in range(len(s)):
        if s[i] not in result:
            answer.append(-1)
            result[s[i]] = i
        else:
            answer.append(i - result[s[i]])
            result[s[i]] = i
    return answer