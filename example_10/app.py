

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