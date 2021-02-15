
class MonClasse:

    def __init__(self, name, age):
      self.name = name
      self.age = age

mon_object = MonClasse("baddi", 35)


print("Bonjour, je suis {0} et j'ai {1}".format(mon_object.name, mon_object.age))