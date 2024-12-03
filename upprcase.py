string=input("Enter the string")
upper_count=0
lower_count=0
strchar=string.replace(' ','')
for char in strchar:
    if char.isupper():
        upper_count+=1
    else:
        lower_count+=1

print(upper_count)
print(lower_count)

