"""
author:Nikkita Anna George
created on:8/10/24
program for Concatenate string.
"""
first_name=input("Enter your first name")
second_name=input("Enter your second name")
full_name=first_name+" "+second_name
print(full_name)
length=len(first_name)
print(length)
extracted_second_name=full_name[:length]
print(extracted_second_name)
