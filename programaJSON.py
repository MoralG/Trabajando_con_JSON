#------------------------- Importacion de marvel.json ---------------------------

import json

with open("marvel.json") as fichero:

    doc=json.load(fichero)

#--------------------------- Definicion de variables -----------------------------

lista_heroes = []
lista_equipos = []
lista_autores = []
lista_hautor = []
lista_heroe1 = []
lista_heroe2 = []
encontrado = False
comparacion_poder = False
comparacion_equipo = False
comparacion_aliados = False

#------------------------------- Lista de heroes ---------------------------------

for dic in doc:

    lista_heroes.append(dic.get("name"))

#------------------------------- Lista de equipos --------------------------------

for dic in doc:

    for equipo in dic.get("teams"):

        if equipo not in lista_equipos:

            lista_equipos.append(equipo)

#-------------------------------- Lista de autores --------------------------------

for dic in doc:

    for autor in dic.get("authors"):

        if autor not in lista_autores:

            lista_autores.append(autor) 

#----------------------------------------------------------------------------------

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

    if opcion == 1:         # opcion 1: lista heroes

        print("---------------------------------------------------------------------------------")
        print("Opcion 1 elegida (Lista de todos los Heroes)")
        print("---------------------------------------------------------------------------------")
        print("")

        for heroes in lista_heroes:           #recorremos lista_heroes creada al principio

            print(heroes)

    if opcion == 2:

        print("---------------------------------------------------------------------------------")
        print("Opcion 2 elegida (Elige un Heroe y te muestra la suma de sus poderes)")
        print("---------------------------------------------------------------------------------")
        print("")
    
        heroe = input("Introduce un Heroe: ")

        while heroe not in lista_heroes:

            print("")
            print("-------------------------")
            print("ERROR, no existe el heroe")
            print("-------------------------")
            print("")

            lista_heroes = input("Introduce un Heroe: ")

        for dic in doc:

            if heroe == dic.get("name"):

                print("")
                print("Heroe:",heroe)
                print("Nº poderes:",len(dic.get("powers")))
                print("")
                print("---------------------")
            
                mostrar_poderes = input("¿Mostar poderes? y/n   ")

                if mostrar_poderes == "y":
                    
                    print("----------------")
                    
                    for poderes in dic.get("powers"):
                    
                        print(poderes)

    if opcion == 3:

        print("---------------------------------------------------------------------------------")
        print("Opcion 3 elegida (Elige un equipo y te muestra los poderes de todos los miembros de dicho grupo)")
        print("---------------------------------------------------------------------------------")
        print("")

        equipo = input("Introduce un equipo: ")

        while equipo not in lista_equipos:

            print("")
            print("-------------------------")
            print("ERROR, no existe el equipo")
            print("-------------------------")
            print("")

            lista_equipos = input("Introduce un equipo: ")

        for dic in doc:

            if equipo in dic.get("teams"):
                
                print("----------------------")
                print(dic.get("name"))
                print("----------------------")

                for poderes in dic.get("powers"):
                    
                    print(poderes)

                print("")


    if opcion == 4:

        print("---------------------------------------------------------------------------------")
        print("Opcion 4 elegida (Haz una busqueda recursiva en la descripcion)")
        print("---------------------------------------------------------------------------------")
        print("")

        busqueda = input("Introduce una cadena para buscar: ")

        for dic in doc:

            if dic.get("description").count(busqueda) > 0:
                
                print("")
                print("---------------------------------")
                print("Heroe:",dic.get("name"))
                print("Descripcion:",dic.get("description"))
                encontrado = True
        
        if encontrado == False:

            print("")
            print("----------------------------------")
            print("NO SE HAN ENCONTRADO COINCIDENCIAS")
            print("----------------------------------")

    if opcion == 5:

        print("---------------------------------------------------------------------------------")
        print("Opcion 5 elegida (Elige autor y compara los poderes, equipos y compañeros de los heroes que le indiquemos)")
        print("---------------------------------------------------------------------------------")
        print("")

        autor = input("Introduce el autor: ")

        while autor not in lista_autores:
            
            print("")
            print("-------------------------")
            print("ERROR, no existe el autor")
            print("-------------------------")
            print("")
            
            autor = input("Introduce el autor: ")               
        
        print("")
        print("-------------------------")
        print("Autor:",autor)
        print("-------------------------")
        print("")

        for dic in doc:

            if autor in dic.get("authors"):

                print(dic.get("name"))
                lista_hautor.append(dic.get("name"))
        
        heroe1 = input("Introduce el Heroe 1 a comparar: ")

        while heroe1  not in lista_hautor:

            print("")
            print("-------------------------")
            print("ERROR, heroe no listado")
            print("-------------------------")
            print("")

            heroe1 = input("Introduce el Heroe 1 a comparar: ")

        heroe2 = input("Introduce el Heroe 2 a comparar: ")

        while heroe2  not in lista_hautor:

            print("")
            print("-------------------------")
            print("ERROR, heroe no listado")
            print("-------------------------")
            print("")

            heroe2 = input("Introduce el Heroe 2 a comparar: ")

        while heroe2 == heroe1:

            print("")
            print("------------------------------")
            print("ERROR, heroe igual que Heroe 1")
            print("------------------------------")
            print("")

            heroe2 = input("Introduce el Heroe 2 a comparar: ")
        
        for dic in doc:

            if dic.get("name") == heroe1:
                
                lista_heroe1 = [dic.get("powers"),dic.get("teams"),dic.get("aliases")]
                dic[heroe1] = [lista_heroe1]

            if dic.get("name") == heroe2:

                lista_heroe2 = [dic.get("powers"),dic.get("teams"),dic.get("aliases")]
                dic[heroe2] = [lista_heroe2]

        print("")
        print("---------------- Poderes iguales en ambos Heroes ----------------")
        print("")

        for poder1 in lista_heroe1[0]:

            for poder2 in lista_heroe2[0]:

                    if poder1 == poder2:

                        print(poder1)
                        comparacion_poder = True

        if comparacion_poder == False:
            
            print("NO TIENEN PODERES IGUALES")

        print("")
        print("---------------- Equipos iguales en ambos Heroes ----------------")
        print("")

        for equipo1 in lista_heroe1[1]:

            for equipo2 in lista_heroe2[1]:

                    if equipo1 == equipo2:

                        print(equipo1)
                        comparacion_equipo = True

        if comparacion_equipo == False:
            
            print("NO ESTAN EN NINGUN EQUIPO JUNTOS")

        print("")
        print("----------------------- Aliados en comun ------------------------")
        print("")
        
        for aliado1 in lista_heroe1[2]:

            for aliado2 in lista_heroe2[2]:

                    if aliado1 == aliado2:

                        print(aliado1)
                        comparacion_aliados = True

        if comparacion_aliados == False:
            
            print("NO TIENEN ALIADOS EN COMUN")



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