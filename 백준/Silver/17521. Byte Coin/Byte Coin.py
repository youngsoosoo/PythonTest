n, w = map(int, input().split())

price = []
for _ in range(n):
    price.append(int(input()))

amount = 0

for i in range(n-1):
    if price[i] < price[i+1]:
        if w // price[i] > 0:
            amount = w // price[i]
            w = w - (amount * price[i])
    elif price[i-1] < price[i] and amount > 0:
        w = w + amount * price[i]
        amount = 0

if amount > 0:
    w = w + amount * price[n-1]

print(w)