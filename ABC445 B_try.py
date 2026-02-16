N=int(input())
m=0
S=[]

for i in range(N):
  S.append(input())
  if len(S[i])>m:
    m=len(S[i])
    

for i in range(N):
  for j in range(((m-len(S[i]))//2)):
    S[i]="."+S[i]+"."
    
  print(S[i])
