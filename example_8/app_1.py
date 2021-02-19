class User:

    def __init__(self, nom, prenom, age, email):
        self.nom = nom
        self.prenom = prenom
        self._age = age
        self.email = email

    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, new_age):
        if new_age>=0:
            self._age = new_age
        else:
            print("l'age ne peut pas etre snegatif")


user =User('baddi', 'youssef', 24, 'baddi@gmail.com')
print(user.age)
user.age=40
print(user.age)


