class Vehiculos():
    
    def __init__(self, marca, modelo):
        
        self.marca=marca
        self.modelo=modelo
        self.enmarcha=False
        self.acelera=False
        self.frena=False
        
    def arrancar(self):
        
        self.enmarcha=True
        
    def acelerar(self):
        
        self.acelera=True
        
    def frenar(self):
        
        self.frena=True

    def estado(self):
        
        print('Marca:', self.marca, '\nModelo:', self.modelo)
        
 
class Moto(Vehiculos):
    pass

miMoto=Moto('Honda', 'CBR')

miMoto.estado()

miVehiculo=Vehiculos('Toyota','HiLux')

miVehiculo.estado()

print("hola")

print ("GihHub comentario")
print ("Prueba que funciona")

print("Saludos a todos, porque si")
