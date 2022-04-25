
def get_key(val):
    for key, value in Dic.items():
         if val == value:
             del Dic[key]
             return key
    
    return "key doesn't exist"


str = input()

length = len(str)
Dic = {}

for i in range(length):
    if str[i] not in str[: i]:
        Dic.update({ str[i] : str.count(str[i]) })


# seperate keys and values from dictionary
key_list = list(Dic.keys())
value_list = list(Dic.values())

value_list.sort(reverse=True)

for i in value_list:
    print(get_key(i) , i)
