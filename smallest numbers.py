

number1=int(input("Enter your first number:"))
number2=int(input("Enter your second number:"))
number3=int(input("Enter your third number:"))
if number1<number2 and number1<number3:
    print("The smallest number is:",number1)
elif number2<number1 and number2<number3:
    print("The smallest number is:", number2)
else:
    print("The smallest number is:", number3)
