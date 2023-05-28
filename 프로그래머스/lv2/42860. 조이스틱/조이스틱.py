### 문제 인식 ###
# 조이스틱을 통해 주어진 문자열의 길이 * A를 주어진 문자열 name을 만들어야 합니다.
# 위랑 아래로 조이스틱을 움직이면 알파벳이 앞 뒤로 움직입니다.
# 왼쪽은 A로 바꿔주지만 A에서 왼쪽으로 움직인다면 Z가 됩니다.
# 오른쪽은 Z로 바꿔주지만 Z에서 오른쪽으로 움직인다면 A가 됩니다.
### 문제 해결 ###
# 조이스틱 조작 횟수
# 기본 최소 좌우이동 횟수는 길이 - 1
# 해당 알파벳 변경 최솟값 추가
# 해당 알파벳 다음부터 연속된 A 문자열 찾기
# 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
# 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가

def solution(name):

	# 조이스틱 조작 횟수 
    answer = 0
    
    # 기본 최소 좌우이동 횟수는 길이 - 1
    min_move = len(name) - 1
    
    for i, char in enumerate(name):
    	# 해당 알파벳 변경 최솟값 추가
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        
        # 해당 알파벳 다음부터 연속된 A 문자열 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1
            
        # 기존, 연속된 A의 왼쪽시작 방식, 연속된 A의 오른쪽시작 방식 비교 및 갱신
        min_move = min([min_move, 2 *i + len(name) - next, i + 2 * (len(name) -next)])
        
    # 알파벳 변경(상하이동) 횟수에 좌우이동 횟수 추가
    answer += min_move
    return answer