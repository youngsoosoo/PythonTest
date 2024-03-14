from itertools import product
def solution(users, emoticons):
    answer = [0, 0]
    discount = [10, 20, 30, 40]
    discount_product = []
    
    # 모든 할인율 조합
    for i in product(discount, repeat=len(emoticons)):
        discount_product.append(i)
        
    for dis in discount_product:
        # [이모티콘 가입자 수, 판매금액]
        sales = [0, 0]
        for user in users:
            # 판매 금액
            pay = 0
            for j in range(len(emoticons)):
                if user[0] <= dis[j]:
                    pay += emoticons[j] * (100-dis[j])//100
                if pay >= user[1]:
                    pay = 0
                    sales[0] += 1
                    break
            sales[1] += pay
        
        if (answer[0] < sales[0]) or(answer[0] == sales[0] and answer[1] < sales[1]):
            answer = sales
    
    
    return answer