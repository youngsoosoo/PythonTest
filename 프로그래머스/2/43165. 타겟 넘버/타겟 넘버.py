from collections import deque

def solution(numbers, target):
    answer = 0
    n = len(numbers)
    que = deque()
    # (idx, 현재값)
    que.append((0, 0))
    
    while que:
        idx, value = que.popleft()
        # idx가 끝까지 가면 종료
        if idx == n:
            if value == target:
                answer+=1
            continue
        
        que.append((idx+1, value - numbers[idx]))
        que.append((idx+1, value + numbers[idx]))
        
    
    return answer