from time import strftime,sleep
def sucesionUlam(num):
    #!Sumar el numero a la lista desde la llamada print([var] + sucesionUlam(var))
    if num==1:
        return []
    if num>40:
        num=40
    if num%2==0:
        num=num//2
        return [num] + sucesionUlam(num)
    if not num%2==0:
        num=num*3 + 1
        if num>40:
           num=40
        return [num] + sucesionUlam(num)

def grabarChats(nomArchGrabar,listaUlam,listaFrases,listaContactos):
    """
    Funcion:Guarda el archivo 
    Entrada:El nombre del archivo y la lista con los elementos
    Salida:nada o un mensaje de error
    """
    nomArchGrabar+=".txt"
    #try:
    f=open(nomArchGrabar,"w",encoding="utf-8")
    f.writelines("#"+str(listaUlam))
    f.writelines("#Extraido de: https://amazonia-teamfactory.com/blog/las-50-mejores-frases-de-motivacion-en-el-trabajo/")    
    contacto=0
    for i in listaUlam:
        if contacto==0:
            contacto=1
        else:
            contacto=0
        hora=strftime("%H:%M:%S")
        f.writelines(str(hora)+"\t De "+str(listaContactos[contacto].nombre)+str(listaContactos[contacto].apellidos)+": "+str(listaFrases[i]))
        sleep(0.3)
    f.close()
    return ""