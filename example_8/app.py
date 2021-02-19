class User:

    def __init__(self, nom, prenom, age, email):
        self.nom = nom
        self.prenom = prenom
        self._age = age
        self.email = email

    def get_age(self):
        return self._age

    def set_age(self, new_age):
        if new_age >= 0:
            self._age=new_age
        else:
            self._age =0
    


class Person(User):
    pass

user =User('baddi', 'youssef', 24, 'baddi@gmail.com')


user.set_age(40)
print(user.get_age())

p =Person('baddi', 'youssef', 25, 'baddi@gmail.com')
print(p.get_age())
