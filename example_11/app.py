

numbers = [1,2,3,4,5,6,7,8,9]

def carre(x): return x ** 2      # one line insctruction
def cube(x): return x ** 3      # one line insctruction

def pair(x): return not bool(x % 2)

def impair(x): return bool(x % 2)

def map(callback, liste):
    new_liste=[]
    for item in liste:
        new_liste.append(callback(item))
    return new_liste

def filter(callback, liste):
    new_liste=[]
    for item in liste:
        if callback(item): new_liste.append(item)
    return new_liste
    

print(map(carre,numbers))
print(map(cube,numbers))

print(filter(pair,numbers))
print(filter(impair,numbers))


def sum(x,y): return x+y
def produit(x,y): return x*y
def sum_1(element,liste): return liste + [element ** 2]

def reduce(callback,liste, init_value): 
    if liste == [] : return init_value
    else: return callback(liste[0], reduce(callback,liste[1:], init_value))

print(reduce(sum,numbers,0))
print(reduce(produit,numbers,1))
print(reduce(sum_1,numbers,[]).reverse())

print([x ** 2 for x in numbers])

print([x for x in numbers if x%2 ==0])

print([x ** 2 for x in numbers if x ** 2 %2 ==0])
print("----")
print([x for x in [y ** 2 for y in numbers] if x %2 ==0])

list_2 = ['b','o','n','j','o','u','r']
print(''.join(list_2))
print(','.join(list_2))
print('b o u n j o u r'.split(' '))

# function returning multiple values
def getInformation(): 
    name='baddi'
    prenom = 'youssef'
    age = 24
    return name, prenom, age

#  date and time format
import time
first_time = time.time()
timenow = time.localtime(time.time())
print(time.time()) # the number of seconde after the 1 Sept 1970
print(timenow)
year,month,day,hour,minute,sec = timenow[0:6]
print("{0}/{1}/{2} {3}:{4}:{5}".format(year,month,day,hour,minute,sec))
time.sleep(5)
second_time = time.time()
print("this need {0} sec to be excuted".format(second_time - first_time))