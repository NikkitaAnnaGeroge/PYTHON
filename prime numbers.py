check_prime=int(input("Enter a number"))
isPrime=True

for i in range (2,check_prime//2+1):
    if check_prime %i ==0:
        isPrime=False
        break
if isPrime:
    print(f"the  given number {check_prime} is prime")
else:
    print(f"the given number{check_prime} is not a prime")

