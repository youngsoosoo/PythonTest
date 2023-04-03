from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 1
    truck = deque([[truck_weights[0], answer]])
    cnt=1
    while True:

        if len(truck) > 0 and truck[0][1] >= bridge_length:
            truck.popleft()
            continue
        
        for i in range(len(truck)):
            truck[i][1] += 1
        answer+=1
        
        if len(truck_weights) == cnt and len(truck) == 0:
            break
        if cnt < len(truck_weights) and len(truck)+1 <= bridge_length and sum(x[0] for x in truck) + truck_weights[cnt] <= weight:
            truck.append([truck_weights[cnt], 1])
            cnt+=1
            
    return answer