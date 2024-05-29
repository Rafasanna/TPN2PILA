class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, item):
        self.items.append(item)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

    def ver_tope(self):
        if not self.esta_vacia():
            return self.items[-1]


def interseccion_pilas(pila1, pila2):
    interseccion = Pila()
    temp = Pila()

    
    while not pila1.esta_vacia():
        temp.apilar(pila1.desapilar())

    
    while not temp.esta_vacia():
        elemento = temp.desapilar()
        if elemento in pila2.items:
            interseccion.apilar(elemento)

    return interseccion


def crear_pila(episodio):
    pila = Pila()
    if episodio == "V":
        
        personajes_v = ["Luke Skywalker", "Darth Vader", "Han Solo", "Princess Leia", "Yoda", "Chewbacca"]
        for personaje in personajes_v:
            pila.apilar(personaje)
    elif episodio == "VII":
        
        personajes_vii = ["Rey", "Finn", "Kylo Ren", "Poe Dameron", "BB-8", "Chewbacca"]
        for personaje in personajes_vii:
            pila.apilar(personaje)
    return pila



pila_v = crear_pila("V")
pila_vii = crear_pila("VII")


interseccion = interseccion_pilas(pila_v, pila_vii)


print("Personajes que aparecen en ambos episodios:")
while not interseccion.esta_vacia():
    print(interseccion.desapilar())
