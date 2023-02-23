from collections import deque

def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    for i in goal:
        if cards1 and cards1[0] == i:
            cards1.popleft()
        elif cards2 and cards2[0] == i:
            cards2.popleft()
        else:
            return "No"
    return "Yes"