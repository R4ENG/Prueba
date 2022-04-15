class Analog():
    
    def __init__(self, nombre, valor, __RawMin, __RawMax, __EngMin, __EngMax):
       
        self.__AlarmaOutRange=False
        self.nombre=nombre
        self.inPut=valor
        self.__RawMin=__RawMin
        self.__RawMax=__RawMax
        self.__EngMin=__EngMin
        self.__EngMax=__EngMax
    
    def identificador(self):

        print('El tag del equipo es:', self.nombre)
        
    def resultante(self):
        
        resultado = ((self.inPut - self.__RawMin)*((self.__EngMax-self.__EngMin)/(self.__RawMax-self.__RawMin)))+self.__EngMin
        print(self.nombre)
        print(resultado)
        if (resultado > self.__EngMax):
            print('Error de instrumento')
            self.__AlarmaOutRange=True
        else:
            pass
        if (resultado < self.__EngMin):
            print('Error de instrumeento')
            self.__AlarmaOutRange=True
        else:
            pass
            
PIT1000=Analog('PIT-1000', 20, 4, 20, 0, 100)
PIT1000.resultante()

