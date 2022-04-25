# Taking input from the user
intger = []
integer = [int(i) for i in input().split()]

k = int(input())

count=0
for i in range(len(integer)):
    sum=0
    j=i+1
    sum = integer[i]
    for j in range(len(integer)):
        if sum<k :
            if (sum+integer[j])<=k :
                sum += integer[j]

        if sum==k :
            count+=1
            break


print(count)
