from app import Voiture, Audi, Mercedes

marque = input("give the car marque")
print(marque)


obj = Voiture.factory(marque)
obj.drive()

