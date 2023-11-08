def add(*args):
    print(args[1])
    sum = 0
    for n in args:

       sum += n
       print(sum)

add(35,6,5,6,8)

def calculate(n, **kwargs):
    print(kwargs)

    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    # print(kwargs["add"])
    n+= kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2,add=3,multiply=6, div=7)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
"""
#  In case when use a square [] and one of args is not assign console return a fault "KeyError"
#  So, in this case better way is using a "get" method on function arguments e.g self.make = km.get("make")
#  When is using method get and call argument isn't found in input tuple Console return a None status ! Without an Error
"""

my_car = Car( make="Nissan", model="GT_R")
print(my_car.model)