import json

with open("marvel.json") as fichero:

    doc=json.load(fichero)

print(doc)


print("")
print("-------------------MENU--------------------")
print("(1) Mostrar todos los Heroes")
print("(2) Contar poderes de Heroes")
print("(3) Poderes de los Heroes de un equipo")
print("(4) Buscar por descripcion")
print("(5) Comparacion entre dos heroes")
print("(0) Finalizar el programa")
print("-------------------------------------------")
print("")