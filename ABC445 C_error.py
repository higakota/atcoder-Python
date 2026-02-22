N=int(input())
A=list(map(int,input().split()))
A=[a-1 for a in A]
B=A.copy()

for i in range(N):
  for _ in range(10**100):
      B[i]=A[B[i]]
      
  print(B[i]+1)
