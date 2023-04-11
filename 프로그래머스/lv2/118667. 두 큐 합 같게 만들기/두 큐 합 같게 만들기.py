from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    

    lq1 = len(queue1)
    lq2 = len(queue2)
    limit = (lq1)*4
    sq1 = sum(queue1)
    sq2 = sum(queue2)

    while sq1 != sq2:
        if (lq1 == 1 and sq1 > sq2) or (lq2 == 1 and sq2 > sq1) or answer == limit:
            return -1

        if sq1 > sq2:
            p = queue1.popleft()
            queue2.append(p)
            sq1 -= p
            lq1 -= 1
            sq2 += p
            lq2 += 1
        else:
            p = queue2.popleft()
            queue1.append(p)
            sq1 += p
            lq1 += 1
            sq2 -= p
            lq2 -= 1

        answer += 1

    return answer
