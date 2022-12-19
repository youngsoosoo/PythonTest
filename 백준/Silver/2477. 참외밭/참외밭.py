import sys
input = sys.stdin.readline

k=int(input())

arr = []
for i in range(6):
	x, y = map(int, input().split())
	arr.append(y)

mw = max(arr)
mh = arr[(arr.index(mw)-1)%6] if arr[(arr.index(mw)-1)%6] > arr[(arr.index(mw)+1)%6] else arr[(arr.index(mw)+1)%6] 

nw = abs(arr[(arr.index(mw)-1)%6]-arr[(arr.index(mw)+1)%6])
nh = abs(arr[(arr.index(mh)-1)%6]-arr[(arr.index(mh)+1)%6])

result = ((mw * mh) - (nw * nh)) * k
print(result)