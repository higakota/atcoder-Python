A=[list(map(int,input().split())) for _ in range(3)]

result=0
counter1={}
counter2={}
counter3={}

for num in A[0]:
        counter1[num] = counter1.get(num, 0) + 1

for num in A[1]:
        counter2[num] = counter2.get(num, 0) + 1

for num in A[2]:
        counter3[num] = counter3.get(num, 0) + 1


if counter1.get(4, 0) > 0 and counter2.get(5, 0) > 0 and counter3.get(6, 0) > 0:
        result+= counter1[4]/6*counter2[5]/6*counter3[6]/6

if counter1.get(4, 0) > 0 and counter2.get(6, 0) > 0 and counter3.get(5, 0) > 0:
        result+= counter1[4]/6*counter2[6]/6*counter3[5]/6

if counter1.get(5, 0) > 0 and counter2.get(4, 0) > 0 and counter3.get(6, 0) > 0:
        result+= counter1[5]/6*counter2[4]/6*counter3[6]/6

if counter1.get(5, 0) > 0 and counter2.get(6, 0) > 0 and counter3.get(4, 0) > 0:
        result+= counter1[5]/6*counter2[6]/6*counter3[4]/6

if counter1.get(6, 0) > 0 and counter2.get(4, 0) > 0 and counter3.get(5, 0) > 0:
        result+= counter1[6]/6*counter2[4]/6*counter3[5]/6

if counter1.get(6, 0) > 0 and counter2.get(5, 0) > 0 and counter3.get(4, 0) > 0:
        result+= counter1[6]/6*counter2[5]/6*counter3[4]/6

print(result)
