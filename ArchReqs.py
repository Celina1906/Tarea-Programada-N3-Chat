#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 20/01/2021 6:40pm 
#Fecha de última Modificación: 21/01/2021 5:02pm
#Versión: 3.9.0
#Importaciones
import requests
import re
from bs4 import BeautifulSoup

def obtenerFrases():
    '''
    Funcionamiento: Por medio de solicitudes HTML extrae las carreras ofrecidas en el tec
    Entradas: NA
    Salidas: Matriz con carreras
    '''
    lista=[]
    r = requests.get('https://amazonia-teamfactory.com/blog/las-50-mejores-frases-de-motivacion-en-el-trabajo/')
    contenido = r.text
    contenido= contenido.rsplit('\n')
    cont=-1
    for i in contenido:
        cont+=1
        if '''<p>1.- De todas las cosas que llevas puestas, tu <strong>actitud</strong> es la más importante.</p>''' in i:
            while contenido[cont]!='''<img loading="lazy" class="alignnone size-full wp-image-5196" src="https://amazonia-teamfactory.com/wp-content/uploads/2017/11/10.png" alt="" width="1200" height="200" srcset="https://amazonia-teamfactory.com/wp-content/uploads/2017/11/10.png 1200w, https://amazonia-teamfactory.com/wp-content/uploads/2017/11/10-300x50.png 300w, https://amazonia-teamfactory.com/wp-content/uploads/2017/11/10-768x128.png 768w, https://amazonia-teamfactory.com/wp-content/uploads/2017/11/10-1024x171.png 1024w" sizes="(max-width: 1200px) 100vw, 1200px" />''':
                vTemp=contenido[cont]
                if "<img loading=" in vTemp:
                    cont+=1
                    continue
                if "<strong>" in vTemp:
                    vTemp= vTemp.replace("<strong>","")
                    vTemp= vTemp.replace("</strong>","")
                soup = BeautifulSoup(vTemp, 'html.parser')
                lista+=[soup.p.string]
                cont+=1
    return lista

