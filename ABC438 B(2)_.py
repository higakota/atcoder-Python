N,M=map(int,input().split())

s=input()
S=[int(x) for x in s]

t=input()
T=[int(x) for x in t]

min=10**9


for i in range(N-M+1):
    Sum=0
    for j in range(M):
       Sum+=S[i+j]-T[j]
       if S[i+j]-T[j]<0:
          Sum+=10

    if Sum<min:
        min=Sum

print(min)
