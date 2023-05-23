### 문제 인식 ###
# 디펜스 게임에서 매 라운드마다 enemy[i] 만큼의 적이 등장.
# 준호가 최대로 상대할 수 있는 병사의 수는 n
# 대신 한 라운드를 통과할 수 있는 무적권이 k개.
# 최대 몇 라운드를 막을 수 있는지 구해라.
### 문제 해결 ###
# 막을 수 있다면 n을 통해 막고 막을 수 없는 수만 무적권 사용(그리디) X
# 무적권을 적절한 시기에 사용해줘야함.(힙, 우선순위 큐)
# 값을 넣는 과정에 남아있는 값(n)과 계산해주고 있는 값(sum_enemy)을 비교합니다.
# True라면 k로 없애줌(우선순위가 높기 때문)
import heapq as hq
def solution(n, k, enemy):
    answer, sum_enemy = 0, 0
    x=[]
    for i in enemy:
        hq.heappush(x, -i)
        sum_enemy += i
        if sum_enemy > n:
            if k == 0:
                break
            hx = hq.heappop(x)

            sum_enemy += hx
            k-=1
        answer += 1

    return answer