"""
author:Nikkita anna
created on:29/11/24
program to check whether the mobile number is valid or invalid
"""

def mobile_number():
    mobile_number=input("Enter the mobile number:")
    length= len(mobile_number)
    if length==10 and   mobile_number[0]=="7"or mobile_number[0]=="8" or mobile_number[0]=="9":
            print("Entered mobile number is valid")
    else:
            print("Entered mobile number is invalid")


mobile_number()
mobile_number()
mobile_number()
mobile_number()
mobile_number()
mobile_number()
mobile_number()
mobile_number()
mobile_number()
mobile_number()
