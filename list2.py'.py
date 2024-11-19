list_1=[]
list_2=[]
list_1size=int(input("Enter the size of the list1:"))
print("Enter the elements of list_1 are:")
for i in range(list_1size):
    list_1.append(int(input()))

print(list_1)
list_2size=int(input("Enter the size of the list2:"))
print("enter the elements of list_2 are:")
for j in range(list_2size):
    list_2.append(int(input()))
print(list_2)
combined_list=list_1+list_2
print(combined_list)
even_list=[]
odd_list=[]
for i in combined_list:
    if i % 2==0:
        (even_list.append(i))
    else:
        (odd_list.append(i))
print(even_list)
print(odd_list)







