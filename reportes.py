#Importaciones
import csv
from archivos import leeChat
#Funciones
def reporte1(lista):
    '''
    Funcionamiento: crea la base de datos en Excel
    Entradas: dicccionario de primeros ingresos y matriz de mentores
    Salidas: nombre del archico .csv
    '''
    nombreArchivo="ReporteContactosDelSistema"+".csv"
    with open(str(nombreArchivo),"w",newline="") as csvfile:
        nombreDeCampos=["Nombre","Apellidos","Tipo","Numero","Correos"]
        escribir= csv.DictWriter(csvfile,fieldnames=nombreDeCampos)
        escribir.writeheader()
        for i in lista:
            escribir.writerow({"Nombre":i.nombre,"Apellidos":i.apellidos,"Tipo":str(i.tipo),"Numero":str(i.numero),"Correos":str(i.correo)})
        return nombreArchivo
        
def reporte2(lista):
    '''
    Funcionamiento: crea la base de datos en Excel
    Entradas: dicccionario de primeros ingresos y matriz de mentores
    Salidas: nombre del archico .csv
    '''
    nombreArchivo="ReporteSiCelular"+".csv"
    with open(str(nombreArchivo),"w",newline="") as csvfile:
        nombreDeCampos=["Nombre","Apellidos","Tipo","Numero","Correo"]
        escribir= csv.DictWriter(csvfile,fieldnames=nombreDeCampos)
        escribir.writeheader()
        for i in lista:
            if i.tipo==1:
                escribir.writerow({"Nombre":i.nombre,"Apellidos":i.apellidos,"Tipo":str(i.tipo),"Numero":str(i.numero),"Correo":str(i.correo)})
        return ""

def reporte3(lista):
    '''
    Funcionamiento: crea la base de datos en Excel
    Entradas: dicccionario de primeros ingresos y matriz de mentores
    Salidas: nombre del archico .csv
    '''
    nombreArchivo="ReporteMayorCantCorreos"+".csv"
    with open(str(nombreArchivo),"w",newline="") as csvfile:
        nombreDeCampos=["Nombre","Apellidos","Tipo","Numero","Correo"]
        escribir= csv.DictWriter(csvfile,fieldnames=nombreDeCampos)
        escribir.writeheader()
        cantCorreos=revisarMaxCorreos(lista)
        for i in lista:
            if len(i.correo)==cantCorreos:
                escribir.writerow({"Nombre":i.nombre,"Apellidos":i.apellidos,"Tipo":str(i.tipo),"Numero":str(i.numero),"Correo":str(i.correo)})
        return ""

def reporte4(listaFrases):
    '''
    Funcionamiento: crea la base de datos en Excel
    Entradas: dicccionario de primeros ingresos y matriz de mentores
    Salidas: nombre del archico .csv
    '''
    nombreArchivo="ReporteFrases"+".csv"
    with open(str(nombreArchivo),"w",newline="") as csvfile:
        nombreDeCampos=["Frase más larga","Frase más corta"]
        escribir= csv.DictWriter(csvfile,fieldnames=nombreDeCampos)
        escribir.writeheader()
        escribir.writerow({"Frase más larga":MayorFrase(listaFrases),"Frase más corta":MenorFrase(listaFrases)})
        return ""

def reporte5(matriz):
    print(matriz)
    '''
    Funcionamiento: crea la base de datos en Excel
    Entradas: dicccionario de primeros ingresos y matriz de mentores
    Salidas: nombre del archico .csv
    '''
    nombreArchivo="ReporteContactosConChat"+".csv"
    with open(str(nombreArchivo),"w",newline="") as csvfile:
        nombreDeCampos=["Numero","Nombre Completo","Nombre del archivo","Cantidad de mensajes en chat"]
        escribir= csv.DictWriter(csvfile,fieldnames=nombreDeCampos)
        escribir.writeheader()
        for i in matriz:
            escribir.writerow({"Numero":i[0][0].numero,"Nombre Completo":str(i[0][0].nombre) + str(i[0][0].apellidos),"Nombre del archivo":"Chat"+ str(i[1]),"Cantidad de mensajes en chat":i[2]})
            escribir.writerow({"Numero":i[0][1].numero,"Nombre Completo":str(i[0][1].nombre) + str(i[0][1].apellidos),"Nombre del archivo":"Chat"+ str(i[1]),"Cantidad de mensajes en chat":i[2]})
        return ""

def reporte6(matriz):
    #En caso de repetidos, imprime el ultimo mayor.
    maxMsj=0
    ultimoConMax=0
    for i in matriz:
        if i[2]>maxMsj:
            maxMsj=i[2]
            ultimoConMax=i[1]
    nomArchGrabar="Chat"+str(ultimoConMax)+".txt"
    contenido=leeChat(nomArchGrabar)
    print(contenido)
    return ""

def MayorFrase(listaFrases):
    cantDig=0
    pos=0
    for i in range(0,len(listaFrases)):
        if len(listaFrases[i])>cantDig:
            pos=i
            cantDig=len(listaFrases[i])
    return listaFrases[pos]

def MenorFrase(listaFrases):
    cantDig=999
    pos=0
    for i in range(0,len(listaFrases)):
        if len(listaFrases[i])<cantDig:
            pos=i
            cantDig=len(listaFrases[i])
    return listaFrases[pos]

def revisarMaxCorreos(lista):
    cantCorreos=0
    for i in lista:
        if len(i.correo)>=cantCorreos:
            cantCorreos=len(i.correo)
    return cantCorreos
