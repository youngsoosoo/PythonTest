def solution(n, words):
    answer = [0, 0]
    arr=[words[0]]
    for i in range(1, len(words)):
        if words[i] in arr or not (len(words)>1 and words[i-1][-1] == words[i][0]):
            answer[0] = (i%n) + 1
            answer[1] = (i//n) + 1
            break
        arr.append(words[i])

    return answer