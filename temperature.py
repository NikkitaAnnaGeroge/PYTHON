"""
author:created by nikkita anna george
22/10/24
"""

temperature=int(input("Enter the temperature"))
unit=input("Is this in (C)elsius or(F)ahrenheit?")
if (unit=="C"):
    f=(9/5 *temperature)+32
    print(temperature,"(C)elsius is",f,"(F)arenheit")
else:
    c=(5/9 )* (temperature-32)
    print(temperature,"Farenheit is","c,(celsius)")


