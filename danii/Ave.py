from Animal import Animal

class Ave(Animal):
    def __init__(self, Nombre, Peso, año_nacimiento, propietario):
        super().__init__(Nombre,Peso)
        self.nacimiento= año_nacimiento
        self.propietario = propietario
        
    def calcularedad(self):
        edad = 2024-self.nacimiento
        print(edad)
        
        if edad > 5:
            print("Es mayor de edad")
        else :
            print("es menor de edad")
        

ave1 = Ave ('Danii', 3, 2012, 'Daniel')
ave1.calcularedad() 
