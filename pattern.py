limit=int(input("Enter a limit:"))
for i in range (limit):
  for j in range(i):
      print("*",end="")
  print()

limit=int(input("Enter the limit:"))
for i in range(limit,0,-1):
    for j in range(i):
        print("*",end="")
    print()

limit=int(input("Enter your limit:"))
for i in range(1,limit+i):
    for j in range(limit-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()

limit=int(input("Enter your limit:"))
for i in range(limit,0,-1):
    for j in range(limit-i):
        print(" ",end="")
    for k in range(2*i-1):
        print("*",end="")
    print()







