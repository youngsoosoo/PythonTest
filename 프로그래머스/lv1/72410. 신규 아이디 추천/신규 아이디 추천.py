def solution(new_id):
    answer = ''
    new_id = new_id.lower()
    for i in new_id:
        if i in ['-', '_', '.'] or i.isalpha() or i.isdigit():
            answer+=i
        if len(answer) > 1 and answer[-1] == answer[-2] == '.':
            answer = answer[:-1];
    answer = answer.strip('.')
    if answer == '':
        answer+='a'
    if len(answer) > 15:
        answer = answer[:15]
        answer = answer.rstrip('.')
    if len(answer) < 3:
        while len(answer) < 3:
            answer+=answer[-1]
    return answer