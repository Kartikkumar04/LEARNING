a=int(input("Enter number:"))
if a>1 and all(a%i !=0 for i in range(2,a)):
    print("It is a prime number.")
else:
    print("Not a prime number.")