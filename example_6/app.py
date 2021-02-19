# __field__   (un field magic)
# __field
# _field     (variable/methods) prive

# encapsulation: on a des attribut et methodes qui sont prive a la class ainsi aux instance de la class


class User:
    def __init__(self, prenom, nom , age, email):
        self.prenom= prenom
        self.nom= nom
        self.age= age
        self.email= email

    def identity(self):
        return f"Nom: {self.nom} Prenom: {self.prenom}"

    def identityFriend(self, friend):
        return f"Nom: {self.nom} est friend with  {friend}"

user = User('baddi', 'youssef',  24, 'baddi@gmail.com')

print(user.nom)
print(user.identity())

print(user.identityFriend('adil'))