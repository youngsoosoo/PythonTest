def solution(numbers):
    answer = []
    for n in numbers:
        if n % 2 == 0:  # 입력값이 짝수일 때
            answer.append(n+1)
        else:  # 입력값이 홀수일 때
            binary = bin(n)[2:] 
            # 뒤에서부터 처음으로 나오는 '0'의 위치 찾기
            idx = binary.rfind('0')  
            # 모든 자리수가 1인 경우
            if idx == -1:  
                # '10'을 앞에 붙이고, 두번째 자리부터 그대로 사용
                answer.append(int('10'+binary[1:], 2))  
            else:
                # '0' 다음 자리에 '1'을 넣고, 그 뒤의 자리수는 그대로 사용
                answer.append(int(binary[:idx]+'10'+binary[idx+2:], 2)) 
    return answer
