def solution(files):
    answer = []
    for file in files:
        head, number, tail = '', '', ''
        number_check = False
        for f in range(len(file)): # 문자열 자르기
            if file[f].isdigit():  # 처음 나오는 숫자부터는 NUMBER로
                number += file[f]
                number_check = True
            elif not number_check:  # NUMBER가 나오기 전까지는 HEAD
                head += file[f]
            else:               # NUMBER가 이미 나왔고, 숫자가 아닌 문자가 나오면 TAIL
                tail = file[f:]
                break
        answer.append((head, number, tail))  # HEAD, NUMBER, TAIL 하나의 튜플로 저장
    answer.sort(key=lambda x:[x[0].lower(), int(x[1])])
        
    return ["".join(i) for i in answer]