# loop questions like 1-100, even no. b/w 1-20, factors using for and while loop, table upto 10 values, armstrong number, factorial, 
#

#Multiplication Table
#n = int(input("Enter a number: "))
#
#for i in range(1,11,1):
#    print(i*n)


#ARMSTRONG NUMBER
#n = int(input("Enter a number: "))
#n1=n
#sum=0
#while n>0:
#    rem=n%10
#    sum=sum+(rem*rem*rem)
#   n=n//10
#if sum==n1:
#    print("Armstrong Number")
#else:
#    print("Not an Armstrong Number")


#Factorial
#n = int(input("Enter a number: "))
#fact=1
#for i in range(n,1,-1):
#    store=i
#    fact=fact*store
#print(f"Factorial of {n} is {fact}")

#prime number
n = int(input("Enter a number: "))

if n <= 1:
    print(f"{n} is not a prime number.")
else:
    is_prime = True  # We start by assuming it IS prime

    for i in range(2, n):
        if n % i == 0:
            is_prime = False  # Found a divisor, so it's NOT prime
            break             # Stop the loop early!

    if is_prime:
        print(f"{n} is a prime number!")
    else:
        print(f"{n} is not a prime number.")


        #yessurr