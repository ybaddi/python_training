# function

def table_de_multiplication(texte, nombre):
    print(texte)
    print(nombre)

def table_de_multiplication_1(nombre, texte='Bonjour,'):
    print(texte)
    print(nombre)

def table_de_multiplication_2(texte='Bonjour,', nombre=3):
    print(texte)
    print(nombre)

def table_de_multiplication_3(nombre=3):
    for i in range(10):
        print("{0} * {1} = {2}".format(i, nombre, i*nombre))

def table_de_multiplication_4(nombre=3):
    return (nombre * 5)