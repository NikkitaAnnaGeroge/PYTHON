lists=[6,9,10,12,9]
unique_lists=[]
for number in lists:
    if number not in unique_lists:
        unique_lists.append(number)
print("The original list is:",lists)
print(unique_lists)





