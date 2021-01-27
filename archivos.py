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