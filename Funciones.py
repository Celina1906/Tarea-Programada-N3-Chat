from time import strftime,sleep
def sucesionUlam(num):
    #!Sumar el numero a la lista desde la llamada print([var] + sucesionUlam(var))
    if num==1:
        return []
    if num>=35:
        num=40
    if num%2==0:
        num=num//2
        return [num] + sucesionUlam(num)
    if not num%2==0:
        num=num*3 + 1
        if num>=35:
           num=40
        return [num] + sucesionUlam(num)
def grabarChats(nomArchGrabar,listaUlam,listaFrases,listaContactos):
    """
    Funcion:Guarda el archivo 
    Entrada:El nombre del archivo y la lista con los elementos
    Salida:nada o un mensaje de error
    """
    nomArchGrabar+=".txt"
    print(nomArchGrabar)
    print(listaUlam)
    print(listaContactos)
    print(len(listaFrases))
    #try:
    f=open(nomArchGrabar,"w",encoding="utf-8")
    f.writelines("#"+str(listaUlam)+"\n")
    f.writelines("#Extraido de: https://amazonia-teamfactory.com/blog/las-50-mejores-frases-de-motivacion-en-el-trabajo/"+"\n")    
    contacto=0
    for i in listaUlam:
        if contacto==0:
            contacto=1
        else:
            contacto=0
        hora=strftime("%H:%M:%S")
        frase=listaFrases[i-1]
        f.writelines(str(hora)+"\t De "+str(listaContactos[contacto].nombre)+" "+str(listaContactos[contacto].apellidos)+": "+frase+"\n")
        sleep(0.3)
    f.close()
    return ""

import random
def buscarPersonas(listaContactos):
    persona1=random.choice(listaContactos)
    persona2=random.choice(listaContactos)
    while persona1==persona2:
        persona2=random.choice(listaContactos)
    return [persona1,persona2]
