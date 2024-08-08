class Animal:
    def __init__(self, Nombre, Peso):
    
      self.Nombre = Nombre
      self.Peso = Peso 
    
    def printname(self):
        print(self.Nombre, self.Peso)
        
x = Animal('Danii', '71.90')
x.printname()