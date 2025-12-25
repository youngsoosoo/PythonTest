from itertools import product

def solution(word):
    words = "AEIOU"
    answer = 0
    
    li = []
    
    def dfs(cnt, w):
        if cnt == 5:
            return
        for i in range(len(words)):
            li.append(w + words[i])
            dfs(cnt + 1, w + words[i])
    
    dfs(0, '')
    
    return li.index(word) + 1