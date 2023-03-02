import sys
input = sys.stdin.readline

n,m=map(int,input().strip().split())
arr=[i for i in range(1,n+1)]
for _ in range(m):
    i,j=map(int,input().strip().split())
    arr=arr[0:i-1]+arr[i-1:j][::-1]+arr[j:]
print(" ".join(str(e) for e in arr))