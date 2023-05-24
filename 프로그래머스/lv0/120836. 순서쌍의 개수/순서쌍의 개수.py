def solution(n):
    answer = set()
    for i in range(1, int(n ** (1 / 2)) + 1):
        if n % i == 0:
            answer.add((i, n//i))
            answer.add((n//i, i))
    return len(answer)