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
def profile(**kwargs):
    print(kwargs) # kwargs is a dict
    for key, value in kwargs.items():
        print(key, "=", value)

profile(name="Amit", age=21, city="Varanasi")
