from collections import Counter
from itertools import combinations

def solution(orders, course):
    answer = []
    for k in course:
        arr = []
        for menu in orders:
            menu_li = list(''.join(menu))
            for li in combinations(menu_li, k):
                res = ''.join(sorted(li))
                arr.append(res)
        arr = Counter(arr).most_common()
        answer += [menu for menu, cnt in arr if cnt > 1 and cnt == arr[0][1]]
    return sorted(answer)