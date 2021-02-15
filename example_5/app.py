class Banque:

    def __init__(self, nom, balance):
      self.nom = nom
      self.balance = balance

    def ajouter_argent(self, montant):
        self.balance += montant
        print("Vous avez ajouter {0} $ au compte en banque de {1}".format(montant, self.nom))

# client_01 = Banque()
# client_01.nom = "Baddi"
# client_01.balance = 20

client_02 = Banque("Baddi",20)
print(client_02.nom)
print(client_02.balance)
client_02.ajouter_argent(10)
# print(client_01.nom)
# print(client_01.balance)
print(client_02.balance)