import math

# Taking input from the user
num_list = []
num_list = [int(i) for i in input().split()]

length = len(num_list)
num_list.sort()

mean = sum(num_list) / length
varience = sum( (i-mean)**2 for i in num_list ) / length
std_dev = math.sqrt(varience)

print(num_list[0], num_list[length-1], round(mean,2), round(std_dev,2), round(varience,2) )
