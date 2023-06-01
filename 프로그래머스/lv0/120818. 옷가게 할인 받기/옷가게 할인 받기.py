import math
def solution(price):
    if price >= 500000:
        price-=price*20/100
    elif price >= 300000:
        price-=price*10/100
    elif price >= 100000:
        price-=price*5/100
    return math.floor(price)