list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
new_list = []
for e in list1:
    if(e in list2):
        pass
    else:
        new_list.append(e)

for e in list2:
    if(e in list1):
        pass
    else:
        new_list.append(e) 
    
print(new_list)

