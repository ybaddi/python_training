class Voiture:

    def factory(type):
        if type == 'Audi':
            return Audi()
        elif type == 'Mercedes':
            return Mercedes()
    
    factory = staticmethod(factory)

class Mercedes(Voiture):
    def drive(self):
        print("Iam Mercedes")
        

class Audi(Voiture):
    def drive(self):
        print("Iam Audi")
    
    

