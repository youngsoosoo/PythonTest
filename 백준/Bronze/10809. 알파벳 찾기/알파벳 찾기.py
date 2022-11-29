S = input()
A = list(range(97, 123)) #아스키코드 숫자 범위

for i in A :
  print(S.find(chr(i)), end=" ")