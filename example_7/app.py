# __field__   (un field magic)
# __field
# _field     (variable/methods) prive

# encapsulation: on a des attribut et methodes qui sont prive a la class ainsi aux instance de la class


class Animal:

    def animal_sounds(self, animal, sound):
        print(f"l'animal {animal} dit {sound}")


class Chat(Animal):
    pass

class Chien(Animal):
    pass


animal = Animal()
animal.animal_sounds("chat", "Miaw")

chat = Chat()
chat.animal_sounds("chat", "Miaw")

chien = Chien()
chien.animal_sounds("Chien", "Waof")