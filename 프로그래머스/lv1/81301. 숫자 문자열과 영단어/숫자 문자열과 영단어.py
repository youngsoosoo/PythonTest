def solution(s):
    answer = ''
    a=''
    arr=['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    dic={}
    for i in range(10):
        dic[arr[i]] = i 
    for i in s:
        if i.isdigit():
            answer+=i
        elif i.isalpha():
            a+=i
            if a in dic.keys():
                answer+=str(dic[a])
                a=''
    answer=int(answer)
    return answer