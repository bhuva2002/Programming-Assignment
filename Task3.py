# Taking input from the user
height = []
height = [int(i) for i in input().split()]

area=0
for i in range(len(height)):
    j=i+1
    for j in range(len(height)):
        if height[i] <= height[j] :
            ans=height[i]*(j-i)
            if ans>area :
                area = ans

        else:
            ans=height[j]*(j-i)
            if ans>area :
                area = ans

print(area)
