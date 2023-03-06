def solution(s):
    answer = 0

    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            a=s[i:j]
            if s[i:j] == a[::-1]:
                answer = max(answer, len(a))
    return answer