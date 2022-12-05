import sys
from collections import Counter
n = int(sys.stdin.readline())
a=[int(sys.stdin.readline()) for _ in range(n)]
a.sort()
print(int(round(sum(a)/n,0)))
print(a[n//2])
f= Counter(a) #딕셔너리 형태로 출력
b = f.most_common()#빈도수가 높은 순으로 튜플 형태로 출력
if len(a)>1:
  if b[0][1] == b[1][1]:#빈도수가 같다면
    print(b[1][0])
  else:
    print(b[0][0])
else:
  print(a[0])

print(a[-1]-a[0])