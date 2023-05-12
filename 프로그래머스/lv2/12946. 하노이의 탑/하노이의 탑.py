### 문제 설명 ###
# 하노이 탑 게임과 같은 규칙을 갖고 있습니다.
# 3개의 꽂을 수 있는 기둥이 있으며 n개의 원판이 있습니다. n은 15이하
# 1번 기둥에 있는 n개의 원판을 움직여 3번 기둥으로 옮길때 리스트에 옮긴 경로를 담아서 리턴해야합니다.

### 문제 해결 ###
# 하노이 탑은 재귀를 구현해서 풀면 될 거 같다.
# 재귀함수를 구현할 때 
# n-1개의 원판을 출발 기둥에서 중간 기둥으로 이동 (재귀 호출)
# n번째 원판을 출발 기둥에서 도착 기둥으로 이동
# n-1개의 원판을 중간 기둥에서 도착 기둥으로 이동 (재귀 호출)
# start는 시작기둥, mid는 중간에 거쳐가는 기둥, end는 도착 기둥, n은 옮길 원판의 수를 의미합니다.

def solution(n):
    answer = []
    
    def hanoi(start, end, mid, n):
        
        if n == 1:
            answer.append([start, end])
        else:
            hanoi(start, mid,end,n-1)
            hanoi(start,end, mid,1)
            hanoi(mid,end,start,n-1)
            
    hanoi(1,3,2,n)
    
    return answer