# This is for default arguments, *args and **kwargs:-

#example code for args:-
#def total(*args):
#    print(args)
#    return sum(args)
#
#print(total(1,2,3))
#print(total(10,20,20,30,40))
#print(total())


#example code for kwargs:-
#def profile(**kwargs):
#    print(kwargs) # kwargs is a dict
#    for key, value in kwargs.items():
#        print(key, "=", value)
#
#profile(name="Amit", age=21, city="Varanasi")


#PRACTICE PROBLEMS:-

#1. Multiply Everything
#def multiply(*args):
#    product = 1
#    for num in args:
#        product = product * num
#    return product
#
#print(multiply(4,5,6,7,))

#2. Count the Arguments
#def how_many(*args):
#    return len(args)
#
#print(how_many(3,2,12,32,41,1))


#3. Greeting with kwargs
#def describe(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key} is {value}")
#
#describe(name="amit")


#yeah