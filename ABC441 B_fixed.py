N,M=map(int,input().split())
S = input()
T = input()
Q = int(input())

for _ in range(Q):
    w = input()
    
    takahashi = all(c in S for c in w)
    aoki = all(c in T for c in w)
    
    if takahashi and not aoki:
        print("Takahashi")
    elif aoki and not takahashi:
        print("Aoki")
    else:
        print("Unknown")
