N=int(input())
T=list(map(int,input().split()))
TI=[]

for i in range(N):
  TI.append((T[i],i+1))
  
TI.sort()
print(TI[0][1], TI[1][1], TI[2][1])
