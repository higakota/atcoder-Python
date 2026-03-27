def puyopuyo(A):
   count=0
   stack=[]

   for s in A:
       stack.append(s)
      
       while len(stack)>=4 and stack[-1]==stack[-2]==stack[-3]==stack[-4]:
          stack.pop()
          stack.pop()
          stack.pop()
          stack.pop()
          

   return stack


N = int(input())

A=list(map(int,input().split()))
result=puyopuyo(A)

print(len(result))
