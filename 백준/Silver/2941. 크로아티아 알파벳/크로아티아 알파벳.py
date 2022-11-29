A = input()
cro = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in cro:
  A = A.replace(i, '*') #input 변수와 동일한 이름의 변수
print(len(A))