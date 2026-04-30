
X=input()
minnum=[]

for x in X:
    minnum.append(x)

minnum.sort()

if minnum[0]=='0':

    for i in range(len(minnum)):
        if minnum[i]!='0':
            minnum[0],minnum[i]=minnum[i],minnum[0]
            break

print(''.join(minnum))
