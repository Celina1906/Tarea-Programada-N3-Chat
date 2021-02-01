#Elaborado por: Leandro Camacho y Celina Madrigal
#Fecha de creación: 27/1/2021 8:01 am
#Fecha de última modificación: 1/2/2021 9:32pm
#Versión 3.9.0
#Importación de librerías:
import pickle
#Definición de funciones
def graba(nomArchGrabar,contactos):
    '''
    Funcionamiento: graba un archivo binario
    Entradas: nombre del archivo y lo que se grabará
    Salidas: NA
    '''
    try:
        f=open(nomArchGrabar,"wb")
        pickle.dump(contactos,f)
        f.close()
    except:
        print("Error al grabar el archivo: ", nomArchGrabar)

def lee (nomArchLeer):
    '''
    Funcionamiento: Función que lee un archivo
    Entradas: nombre del archivo
    Salidas: NA
    '''
    try:
        f=open(nomArchLeer,"rb")
        contactos = pickle.load(f)
        f.close()
    except:
        print("Error al leer el archivo: ", nomArchLeer)
    return contactos

def leeChat (nomArchLeer):
    '''
    Funcionamiento: Función que lee un archivo
    Entradas: nombre del archivo
    Salidas: NA
    '''
    file = open(nomArchLeer, "r",encoding='UTF-8')
    resultado = file.read()
    file.close()

    return resultado

def grabarXml(nomArchGrabar,lista):
    """
    Funcion:Guarda el archivo 
    Entrada:El nombre del archivo y la lista con los elementos
    Salida:nada o un mensaje de error
    """
    nomArchGrabar+=".xml"
    #try:
    f=open(nomArchGrabar,"w",encoding="utf-8")
    f.writelines("<contactos>\n")
    for i in lista:
        f.writelines("\t<nombre>"+i.nombre+"</nombre>\n")
        f.writelines("\t\t<apellidos>"+i.apellidos+"</apellidos>\n")
        f.writelines("\t\t<tipo>"+str(i.tipo)+"</tipo>\n")
        f.writelines("\t\t<numero>"+str(i.numero)+"</numero>\n")
        f.writelines("\t\t<correo>"+str(i.correo)+"</correo>\n")
    f.writelines("</Contactos>\n")
    f.close()
    return ""

        