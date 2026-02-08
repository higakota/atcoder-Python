def DigitSum(x):
  ans=0
  s=str(x)
  
  for c in s:
    ans+=int(c)
    
  return ans
  
  
N,K=map(int,input().split())
ans=0
for i in range(1,N+1):
  if DigitSum(i)==K:
    ans+=1
  
print(ans)
