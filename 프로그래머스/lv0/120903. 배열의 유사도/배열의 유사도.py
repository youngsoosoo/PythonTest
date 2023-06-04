def solution(s1, s2):
    answer = len(s1+s2) - len(set(s1+s2))
    return answer