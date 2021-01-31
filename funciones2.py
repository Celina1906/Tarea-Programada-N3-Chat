import random
def buscarPersonas(listaContactos):
    persona1=random.choice(listaContactos)
    persona2=random.choice(listaContactos)
    while persona1==persona2:
        persona2=random.choice(listaContactos)
    return [persona1,persona2]

