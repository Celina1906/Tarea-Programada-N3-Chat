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
        nombreDeCampos=["Nombre","Apellidos","Tipo","Numero","Correo"]
        escribir= csv.DictWriter(csvfile,fieldnames=nombreDeCampos)
        escribir.writeheader()
        for i in lista:
            escribir.writerow({"Nombre":i.nombre,"Apellidos":i.apellidos,"Tipo":i.tipo,"Numero":i.numero,"Correos":i.correo})
        return nombreArchivo
    
#reporte1([])
#,"Correos":i.correo