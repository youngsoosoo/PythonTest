import sys, collections
input = sys.stdin.readline

deque = collections.deque()
for _ in range(int(input())):
    a = list(map(int,input().split()))

    if a[0] == 1:
        deque.append(a[1])
    elif a[0] == 2:
        deque.appendleft(a[1])
    elif a[0] == 3:
        print(deque.pop() if deque else -1)
    elif a[0] == 4:
        print(deque.popleft() if deque else -1)
    elif a[0] == 5:
        print(len(deque))
    elif a[0] == 6:
        print(0 if deque else 1)
    elif a[0] == 7:
        print(deque[-1] if deque else -1)
    else:
        print(deque[0] if deque else -1)