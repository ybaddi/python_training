import math

class Circle:

    def __init__(self,radius):
        self.__radius = radius

    def setRedius(self, radius):
        self.__radius = radius

    def getRedius(self):
        return self.__radius

    def area(self):
        return math.pi * self.__radius ** 2

    def __add__(self, another_circle):
        return Circle(self.__radius + another_circle.__radius)
    
    def __mul__(self, another_circle):
        return Circle(self.__radius * another_circle.__radius)

# 
# + => add
# - => sub
# * => mul
# % => __mod__
# / => truediv
# < lt
# > gt
# <= le
# == => eq
# != => ne
# >= => ge
c1 = Circle(4)
print(c1.getRedius())

c2 = Circle(5)
print(c2.getRedius())

c3 = c1 + c2
print(c3.getRedius())

c4 = c1 * c2
print(c4.getRedius())


#  formating

print("Float format {0:.2f}".format(346.5678273637))

# 
def sum (x,y): 
    print("sum is ", x+y)

def sum_1 (*args): 
    res = 0
    for i in args:
        res += i
    print("sum is ", res)

def sum_1 (*args): 
    res = 0
    for i in args:
        res += i
    print("sum is ", res)

def sum_2 (**args): 
    res = 0
    for i,j in args.items():
        print(i, j)
        res += j
    print("sum is ", res)

sum(3,4)
sum_1(3,4,5)
sum_1(3,4,5,6)

sum_2(produit_1=10,produit_2=20, produit_3=40)

def sum_3(a, b, c):
    print(a+b+c)

s=[2,3,4,7]
sum_3(*s)