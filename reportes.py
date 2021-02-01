#Importaciones
import csv
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
