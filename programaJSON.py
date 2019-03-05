#------------------------- Importacion de marvel.json ---------------------------

import json

with open("marvel.json") as fichero:

    doc=json.load(fichero)

#--------------------------- Definicion de variables -----------------------------

lista_heroes = []

#------------------------------- Lista de heroes ---------------------------------

for dic in doc:

    lista_heroes.append(dic.get("name"))

#---------------------------------------------------------------------------------

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

opcion = int(input("¿Que opcion eliges?   "))

while opcion != 0:

    if opcion == 1:

        print("---------------------------------------------------------------------------------")
        print("Opcion 1 elegida (Lista de todos los Heroes)")
        print("---------------------------------------------------------------------------------")
        print("")
        
        for heroes in lista_heroes:

            print(heroes)

    if opcion == 2:

        print("---------------------------------------------------------------------------------")
        print("Opcion 2 elegida (Elige un Heroe y te muestra la suma de sus poderes)")
        print("---------------------------------------------------------------------------------")

    
    if opcion == 3:

        print("---------------------------------------------------------------------------------")
        print("Opcion 3 elegida (Elige un equipo y te muestra los poderes de todos los miembros de dicho grupo)")
        print("---------------------------------------------------------------------------------")


    if opcion == 4:

        print("---------------------------------------------------------------------------------")
        print("Opcion 4 elegida (Haz una busqueda recursiva en la descripcion)")
        print("---------------------------------------------------------------------------------")


    if opcion == 5:

        print("---------------------------------------------------------------------------------")
        print("Opcion 5 elegida (Elige autor y compara los poderes, equipos y compañeros de los heroes que le indiquemos)")
        print("---------------------------------------------------------------------------------")


    if opcion < 0 or opcion > 5:

        print("-----------------------")
        print("ERROR, opcion no valida")
        print("-----------------------")

    print("")
    print("")
    print("")
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

    opcion = int(input("¿Que opcion eliges?   "))



print("-----------------------")
print("   FIN DEL PROGRAMA")
print("-----------------------")