import sys
input = sys.stdin.readline

n, w, l = map(int, input().split())
truck = list(map(int, input().split()))

bridge = [0] * w
answer=0

while bridge:
	answer+=1
	bridge.pop(0)
	if truck:
		if sum(bridge) + truck[0] <= l:
			bridge.append(truck.pop(0))
		else:
			bridge.append(0)
print(answer)