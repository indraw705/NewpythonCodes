#
#
# multiple = lambda x,y : x*y
# fact = lambda x : 1 if x==0 else x*fact(x-1)
#
#
# print(multiple(131,41))
# print(multiple(32,14))
# print(multiple(3,14))
# print(multiple(3,1))
#
# print(fact(5))

class fruit:
    def __init__(self):
        print("i'm fruit")

class citrus(fruit):
    def __init__(self):
        super().__init__()
        print("i'm mango")

lemon = citrus()

