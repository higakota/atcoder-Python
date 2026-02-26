N,M=map(int,input().split())

s=input()
S=[int(x) for x in s]

t=input()
T=[int(x) for x in t]

num=N-M+1
min=float('inf')


for k in range(num):
  kari=0  
  for i in range(M):
    diff=S[i+k]-T[i]
    if diff<0:
     kari+=10
    kari+=diff
    
  if kari<min:
   min=kari

print(min)
       
