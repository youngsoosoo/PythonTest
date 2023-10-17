import sys
input = sys.stdin.readline

n = int(input())
card = list(map(int, input().split()))

card.sort()

select2 = max(card[0] * card[1], card[-1] * card[-2])
select3 = max(card[0] * card[1] * card[-1], card[-1] * card[-2] * card[-3])
print(max(select2, select3))