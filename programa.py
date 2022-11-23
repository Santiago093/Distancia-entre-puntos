from punto import Punto

messi=Punto()
elbicho=Punto()


a=messi.Calcular_distancia(elbicho)

messi.x=8
messi.y=2

elbicho.x=9
elbicho.y=9

a=messi.Calcular_distancia(elbicho)
b=elbicho.Calcular_distancia(messi)

print(a, "y" ,b)