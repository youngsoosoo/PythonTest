import math
def solution(numbers, hand):
    left=9
    right=11
    answer = ''
    for i in numbers:
        i=i-1
        if i == -1:
            i=10
        
        if i == 0 or i == 3 or i == 6:
            left = i
            answer+='L'
        elif i == 2 or i == 5 or i == 8:
            right=i
            answer+='R'
        else :#중앙에 숫자가 있을때
            if abs(left//3-i//3)+abs(left%3-i%3) < abs(right//3-i//3)+abs(right%3-i%3):
                left=i
                answer+="L"
            elif abs(left//3-i//3)+abs(left%3-i%3) > abs(right//3-i//3)+abs(right%3-i%3):
                right=i
                answer+="R"
            else:
                if hand=="left":
                    left=i
                    answer+="L"
                else:
                    right=i
                    answer+="R"
                
                
    return answer