N=int(input())
A=list(map(int,input().split()))

A=[a-1 for a in A]

LOG=105

db=[[0]*N for _ in range(LOG)]

for i in range(N):
  db[0][i]=A[i]
  

for k in range(LOG-1):
  for i in range(N):
    db[k+1][i]=db[k][db[k][i]]
    
K=10**100
answer=[]

for i in range(N):
  cur=i
  
  for k in range(LOG):
    if (K>>k)&1:
      cur=db[k][cur]
      
  answer.append(cur+1)
  
print(*answer)
