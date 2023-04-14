def solution(m, musicinfos):
    answer = []
    m = m.replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
    
    for i in musicinfos:
        musicinfo = i.split(',')
        musicinfo[3] = musicinfo[3].replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g").replace("A#", "a")
        l = len(musicinfo[3])
        # 시작 시간
        a = musicinfo[0].split(':')
        # 종료 시간
        b = musicinfo[1].split(':')
        # 재생 시간 정의
        t = (int(b[0])-int(a[0]))*60 + (int(b[1]) - int(a[1]))
        if t < l:
            an = musicinfo[3][:t]
        else:
            an = musicinfo[3]*(t//l) + musicinfo[3][:t%l]

        # 멜로디 일치 여부를 확인한 후, 실제 멜로디가 일치하는지 확인합니다.
        if m in an:
            answer.append([musicinfo[2], t, i])
    answer.sort(key=lambda x: (-x[1],x[0]))

    if answer:
        return answer[0][0]
    else:
        return "(None)"
