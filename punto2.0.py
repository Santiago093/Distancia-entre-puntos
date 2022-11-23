import math
class Punto():
    def __init__ (self):
        self.x=0
        self.y=0
        
    def Calcular_distancia(self,otropunto):
        
        distance=math.sqrt(math.pow((self.x - otropunto.x),2) + math.pow((self.y - otropunto.y),2))
        
        return(distance)
        
        
        
        

        
