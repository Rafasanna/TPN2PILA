#24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
#su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
#necesarias para resolver las siguientes actividades:

#a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición uno la cima de la pila;    
#b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar la cantidad de películas en la que aparece;
#c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
#d. mostrar todos los personajes cuyos nombre empiezan con C, D y G."""

from pila import Pila

personajes_mcu = Pila()
personaje1 = {'nombre': 'Rocket Raccoon', 'peliculas': 5}
personaje2 = {'nombre': 'Groot', 'peliculas': 4}
personaje3 = {'nombre': 'Iron Man', 'peliculas': 10}
personaje4 = {'nombre': 'Black Widow', 'peliculas': 9}
personaje5 = {'nombre': 'Capitan America', 'peliculas': 7}
personaje6 = {'nombre': 'Thor', 'peliculas': 8}
personaje7 = {'nombre': 'Hulk', 'peliculas': 7}
personaje8 = {'nombre': 'Black Panther', 'peliculas': 4}
personaje9 = {'nombre': 'Spider-Man', 'peliculas': 5}
personaje10 = {'nombre': 'Doctor Strange', 'peliculas': 3}
personaje11 = {'nombre': 'Scarlet Witch', 'peliculas': 4}
personaje12 = {'nombre': 'Vision', 'peliculas': 3}
personaje13 = {'nombre': 'Ant-Man', 'peliculas': 3}
personaje14 = {'nombre': 'Wasp', 'peliculas': 2}
personaje15 = {'nombre': 'Capitana Marvel', 'peliculas': 2}
personaje16 = {'nombre': 'Falcon', 'peliculas': 4}
personaje17 = {'nombre': 'Winter Soldier', 'peliculas': 4}

personajes_mcu.push(personaje1)
personajes_mcu.push(personaje2)
personajes_mcu.push(personaje3)
personajes_mcu.push(personaje4)
personajes_mcu.push(personaje5)
personajes_mcu.push(personaje6)
personajes_mcu.push(personaje7)
personajes_mcu.push(personaje8)
personajes_mcu.push(personaje9)
personajes_mcu.push(personaje10)
personajes_mcu.push(personaje11)
personajes_mcu.push(personaje12)
personajes_mcu.push(personaje13)
personajes_mcu.push(personaje14)
personajes_mcu.push(personaje15)
personajes_mcu.push(personaje16)
personajes_mcu.push(personaje17)

def posicion_rocket_groot(pila):
    posicion_rocket = None
    posicion_groot = None
    temp_pila = Pila()

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje['nombre'] == 'Rocket Raccoon':
            posicion_rocket = pila.size() + 1
        if personaje['nombre'] == 'Groot':
            posicion_groot = pila.size() + 1
        temp_pila.push(personaje)

    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    return posicion_rocket, posicion_groot


posicion_rocket, posicion_groot = posicion_rocket_groot(personajes_mcu)
print ("----------------------------------------------------------------------")
print("Posicion de Rocket Raccoon:", posicion_rocket)
print("Posicion de Groot:", posicion_groot)
print ("----------------------------------------------------------------------")

def personajes_mas_de_5_peliculas(pila):
    personajes = []

    while pila.size() > 0:
        personaje = pila.pop()
        if personaje['peliculas'] > 5:
            personajes.append(personaje)

    return personajes

personajes_con_mas_de_5_peliculas = personajes_mas_de_5_peliculas(personajes_mcu)
print ("______________________________________________________________________")
print("Personajes que participaron en mas de 5 peliculas de la saga:")
print ("______________________________________________________________________")

for personaje in personajes_con_mas_de_5_peliculas:
    print("Nombre:", personaje['nombre'])
    print("Cantidad de peliculas:", personaje['peliculas'])
    print ("----------------------------------------------------------------------")


def contar_peliculas_viuda_negra(pila):
    temp_pila = Pila()
    peliculas_viuda_negra = 0

    while pila.size() > 0:
        personaje = pila.pop()
        temp_pila.push(personaje)
        if personaje['nombre'] == 'Black Widow': 
            peliculas_viuda_negra = personaje['peliculas']
           

    while temp_pila.size() > 0:
         pila.push(temp_pila.pop())

    return peliculas_viuda_negra

peliculas_viuda_negra = contar_peliculas_viuda_negra(personajes_mcu)
print ("----------------------------------------------------------------------")
print("Numero de peliculas en las que participo la Viuda Negra:", peliculas_viuda_negra)
print ("----------------------------------------------------------------------")

def mostrar_personajes_inicio_cdg(pila):
    temp_pila = Pila()
    personajes_cdg = []

    while pila.size() > 0:
        personaje = pila.pop()
        temp_pila.push(personaje)
        nombre = personaje['nombre']
        if nombre.startswith('C') or nombre.startswith('D') or nombre.startswith('G'):
            personajes_cdg.append(personaje)

    while temp_pila.size() > 0:
        pila.push(temp_pila.pop())

    return personajes_cdg

personajes_cdg = mostrar_personajes_inicio_cdg(personajes_mcu)

print ("----------------------------------------------------------------------")
print("Personajes cuyos nombres comienzan con C, D o G:")
print ("----------------------------------------------------------------------")
for personaje in personajes_cdg:
    print(personaje['nombre'])
