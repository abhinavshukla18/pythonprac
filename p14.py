# Programs for Exception handling:-

#eg:-

#try:
#    a = int(input("a: "))
#    b = int(input("b: "))
#    z = a/b
#    print(z)
#except ZeroDivisionError:
#    print("Error in division, try again")
#except ValueError:
#    print("Input valid values")
#else:
#    print("No errors hehe")
#finally:
#    print("Hi lol")


#1. Safe Number Input:-
#try:
#    num = int(input("Enter the number: "))
#    double = num*2
#    print("The number is ", double)
#except ValueError:
#    print("Please enter a valid number")

#2. Safe Division :-
#try:    
#    a = int(input("Enter a: "))
#    b = int(input("Enter b: "))
#    x = a/b
#    print(x)
#except ZeroDivisionError:
#    print("b cannot be zero.. enter a valid number")
#except ValueError:
#    print("Enter a valid number")


#3. 