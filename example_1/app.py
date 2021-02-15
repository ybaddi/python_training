# git clone  => cloner un projet from git url
# git status => la situation de ton projet en local, 
#               les folders/fichiers tracked/ untracked, edited (added or deleted)
# git add <folder/file> => il va ajouter l'element pour etre dans l'index du tracking
# git commit -m " "   => ajouter la modification as a commit dans l'index local
# git push           => send all commits to the remote repository

# git checkout
# git pull 

nom = "Johan"
age = 35
mylist = [1,2,3]

print(nom, age)
print("Bonjour, je m'appelle %s" % nom)
print("Bonjour, je m'appelle %s" %(nom))
print("Bonjour, je m'appelle %s et j'ai %d" %(nom,age))
print("Bonjour, my list is %s" % mylist)
# print("Bonjour, je m'appelle %s et j'ai %d" %(age,nom))     ca marche pas
print("Bonjour, je m'appelle {0}".format(nom))
print("Bonjour, je m'appelle {0} et j'ai {1}".format(nom, age))
print("Bonjour, je m'appelle {0} et j'ai {1}. {0} -- {1}".format(nom, age))


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

table_de_multiplication("Bonjour, Baddi",3)
table_de_multiplication(nombre=3, texte="Bonjour, Baddi")
table_de_multiplication_1(3)
table_de_multiplication_2()
table_de_multiplication_2(nombre=2)
table_de_multiplication_3()
print("====")
table_de_multiplication_3(5)
mon_res = table_de_multiplication_4(5)
print(mon_res)
# table_de_multiplication("Bonjour, Baddi")
# table_de_multiplication("au revoir, Baddi")




