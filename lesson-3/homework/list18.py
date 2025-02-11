list1 = [1,2,3,4,5,6,7]
list2 = [10,3,4]
x=1
for i in list2:
    x = x * bool(i in list1)

if(x==1):
    print("Yes")
else:
    print("No") 
    