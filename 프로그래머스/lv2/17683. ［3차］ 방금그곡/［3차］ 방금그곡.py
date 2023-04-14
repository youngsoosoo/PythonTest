def solution(m, musicinfos):
    candidate =[]
    notes ={'C#':'H','D#':'I','F#':'J','G#':'K','A#':'L'}
    for note,new in notes.items():
        m = m.replace(note,new)
    for i,musicinfo in enumerate(musicinfos):
        start,end,name,music = musicinfo.split(',')
        for note, new in notes.items():
            music = music.replace(note,new)
        start, end = list(map(int,start.split(':'))),list(map(int,end.split(':')))
        play_time = (end[0]-start[0])*60 + end[1]-start[1]
        if play_time < len(music):
            music = music[:play_time]
        else:
            music = music*(play_time//len(music)) + music[:(play_time%len(music))]
        if m in music:
            candidate.append([name,play_time,i])
    candidate.sort(key=lambda x: (-x[1],x[0]))
    if candidate:
        return candidate[0][0]
    else:
        return "(None)"