N,M=map(int,input().split())

F=list(map(int,input().split()))

S=set(F)

if len(S)==N:
    print("Yes")

else:
    print("No")

if len(S)==M:
    print("Yes")

else:
    print("No")
