H, M = input().split()
H = int(H)
M = int(M)

if M-45 < 0:
  if H==0:
    print(H+23,60-45+M)
  else:
    print(H-1,60-45+M) 
else :
  print(H,M-45)