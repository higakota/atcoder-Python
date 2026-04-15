
T=int(input())

answer=[]

for _ in range(T):

    N,H=map(int,input().split())
    L=H
    R=H
    nowT=0
    possible = True

    for _ in range(N):
        t,l,u=(map(int,input().split()))

        if not possible:
            continue
        
        Δt=t-nowT
    
        L = max(1, L - Δt)
        R = R + Δt  

        L=max(L,l)
        R=min(R,u)

        if L>R:
            possible=False
        
        nowT=t
    
    if possible:
        answer.append("Yes")

    else:
        answer.append("No")


print("\n".join(answer))
