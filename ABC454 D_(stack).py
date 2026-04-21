import sys
input=sys.stdin.readline

T=int(input())

result=[]
for _ in range(T):
    

    A=str(input())
    B=str(input())

    stackA=[]
    stackB=[]

    for s in A:
        stackA.append(s)

        while len(stackA)>=4 and stackA[-1]==")" and stackA[-2]=="x" and stackA[-3]=="x" and stackA[-4]=="(":
            stackA.pop()
            stackA.pop()
            stackA.pop()
            stackA.pop()
            stackA.append("x")
            stackA.append("x")


    for t in B:
        stackB.append(t)

        while len(stackB)>=4 and stackB[-1]==")" and stackB[-2]=="x" and stackB[-3]=="x" and stackB[-4]=="(":
            stackB.pop()
            stackB.pop()
            stackB.pop()
            stackB.pop()
            stackB.append("x")
            stackB.append("x")


    if stackA==stackB:
        result.append("Yes")

    else:
        result.append("No")


for r in result:
    print(r)
