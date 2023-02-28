def solution(sizes):
    answer = 0
    x=0
    y=0
    for i in sizes:
        if i[0] < i[1]:
            temp=i[0]
            i[0] = i[1]
            i[1] = temp
    for i in sizes:
        x = max(i[0], x)
        y = max(i[1], y)
    answer= x*y
    return answer