def solution(book_time):
    room = []
    
    book_time.sort()
    print(book_time)
    
    for i in book_time:
        
        # 모든 시간을 분 단위로 변경
        for j in range(2):
            time, minute = map(int, i[j].split(':'))
            i[j] = time*60+minute

        flag=0
        
        for j in range(len(room)):
            # 10 분을 더해줌.
            
            if room[j][1] + 10 <= i[0]:
                room[j] = i
                flag=1
                break
        
        if flag == 0:
            room.append(i)

    return len(room)