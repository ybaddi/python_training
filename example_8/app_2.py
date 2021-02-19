class Animal:
    def sound(self):
        raise NotImplementedError("la clkass n'a pas defini la method sound")
    

class Chat(Animal):
    def sound(self):
        print("Moaw")

class Chien(Animal):
    def sound(self):
        print("Woaf")


# animal = Animal()
# animal.sound()

chat = Chat()
chat.sound()


chien = Chien()
chien.sound()

# iterable = un object qui renvoie un loop sur un objet 

def loop(iterable, callback):
    iterateur = iter(iterable)
    while True:
        try:
            obj = next(iterateur)
        except StopIteration:
            break
        else:
            callback(obj)


def computeAdd(x):
    print(x + 1)

def computeCarre(x):
    print(x**2)

def computeCube(x):
    print(x**3)

list = [1,2,3,4,5,6,7,8,9,10]
loop(list, computeCube)
print("---------------")
loop(list, computeCarre)
print("---------------")
loop(list, computeAdd)
print("---------------")

#---------------------------------------------------

# yield

def countDown(debut):
    while debut >= 0:
        yield debut
        debut -= 1

print(countDown(20))

my_countDown = countDown(20)
print(next(my_countDown))
print(next(my_countDown))
print(next(my_countDown))
print("---------------")
for m in my_countDown:
    print(m)


#---------------------------------------------------
# utilisation d'un decorateur, decators
# example 1
#---------------------------------------------------

def speak(param):
    def wrapper():
        print("hello world!")
        param()
        print("ok i accept")
    return wrapper

def sorry():
    print("sorry iam baddi")


hello = speak(sorry)
hello()


#---------------------------------------------------
# utilisation d'un decorateur, decators
# example 1
#---------------------------------------------------

def speak(param):
    def wrapper():
        print("hello world!")
        param()
        print("ok i accept")
    return wrapper

@speak
def sorry():
    print("sorry iam baddi")


# hello = speak(sorry)
# hello()

sorry()


#---------------------------------------------------


