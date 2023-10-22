import sys
input = sys.stdin.readline

n = int(input())

graph = [[] for i in range(130)]

def prerecur(node):
	if node == 46:
		return
	
	print(chr(node), end="")
	prerecur(graph[node][0])
	prerecur(graph[node][1])

def inrecur(node):
	if node == 46:
		return
	
	inrecur(graph[node][0])
	print(chr(node), end="")
	inrecur(graph[node][1])
	
def postrecur(node):
	if node == 46:
		return
	
	postrecur(graph[node][0])
	postrecur(graph[node][1])
	print(chr(node), end="")
	
for _ in range(n):
	a, b, c = map(str, input().split())
	
	a = ord(a)
	b = ord(b)
	c = ord(c)
	
	graph[a].append(b)
	graph[a].append(c)
prerecur(65)
print()
inrecur(65)
print()
postrecur(65)
