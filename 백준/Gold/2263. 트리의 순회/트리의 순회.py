import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

arr = [0] * (n+1)
for i in range(n):
	arr[inorder[i]] = i

def preorder(inStart, inEnd, postStart, postEnd):
	
	if (inStart > inEnd) or (postStart > postEnd):
		return
	
	root = postorder[postEnd]
	print(root, end = " ")
	
	leftNode = arr[root] - inStart
	rightNode = inEnd - arr[root]
	
	preorder(inStart, inStart + leftNode - 1, postStart, postStart + leftNode - 1)
	preorder(inEnd - rightNode + 1, inEnd, postEnd - rightNode, postEnd - 1)
	
preorder(0, n - 1, 0, n - 1)