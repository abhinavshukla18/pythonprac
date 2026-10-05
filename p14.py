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


#3. Safe List Access:-
#items = [10, 20, 30]
#try:
#    ind = int(input("Enter index: "))
#    print(items[ind])
#except IndexError:
#    print("No item there")


#4. Always Say Goodbye:-
#try:
#    a = int(input("Enter a: "))
#    b = int(input("Enter b: "))
#    z = a+b
#    print(z)
#except ValueError:
#    print("Enter valid numbers")
#finally:
#    print("Thank you for using the app")


#5. Keep Asking Until Valid:- 
#while True:
#    try:
#        a = int(input("enter a: "))
#        z = a*2
#        print(z)
#        break
#    except ValueError:
#        print("Enter valid number")

#6: Validate with raise:-
#def set_age(age):
#    if age <0 or age >150:
#        raise ValueError("Not Valid gng TT")
#    return age
#
#try:
#    user_age = set_age(-5)
#    print(f"Age set to: {user_age}")
#except ValueError as error:
#    print(f"Error caught: {error}")

