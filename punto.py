import math
class Punto():
    def __init__ (self):
        self.x=64
        self.y=25
    def Calcular_distancia(self,otropunto):
        
        distance=math.sqrt(math.pow(self.x,otropunto.x) + math.pow(self.y,otropunto.y))
        
        return(distance)
        
        
        
        
mipunto1=Punto()
mipunto1.Calcular_distancia()

mipunto2=Punto()
mipunto2.Calcular_distancia
        
