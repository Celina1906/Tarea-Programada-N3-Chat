#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 20/01/2021 6:40pm 
#Fecha de última Modificación: 1/02/2021 6:46am
#Versión: 3.9.0
#Importaciones
import requests
import re
from bs4 import BeautifulSoup
#Funciones
def obtenerFrases():
    '''
    Funcionamiento: Por medio de solicitudes HTML extrae las frases de la página
    Entradas: NA
    Salidas: lista con frases
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
                if """<img loading="lazy" class="alignnone size-full wp-image-5205" src="https://amazonia-teamfactory.com/wp-content/uploads/2017/11/2.png" alt="" width="1200" height="200" srcset="https://amazonia-teamfactory.com/wp-content/uploads/2017/11/2.png 1200w, https://amazonia-teamfactory.com/wp-content/uploads/2017/11/2-300x50.png 300w, https://amazonia-teamfactory.com/wp-content/uploads/2017/11/2-768x128.png 768w, https://amazonia-teamfactory.com/wp-content/uploads/2017/11/2-1024x171.png 1024w" sizes="(max-width: 1200px) 100vw, 1200px" />""" in vTemp:
                    vTemp= vTemp.replace("<strong>","")
                    vTemp= vTemp.replace("</strong>","")
                    vTemp= vTemp.replace("""<img loading="lazy" class="alignnone size-full wp-image-5205" src="https://amazonia-teamfactory.com/wp-content/uploads/2017/11/2.png" alt="" width="1200" height="200" srcset="https://amazonia-teamfactory.com/wp-content/uploads/2017/11/2.png 1200w, https://amazonia-teamfactory.com/wp-content/uploads/2017/11/2-300x50.png 300w, https://amazonia-teamfactory.com/wp-content/uploads/2017/11/2-768x128.png 768w, https://amazonia-teamfactory.com/wp-content/uploads/2017/11/2-1024x171.png 1024w" sizes="(max-width: 1200px) 100vw, 1200px" />""","")
                    soup = BeautifulSoup(vTemp, 'html.parser')
                    lista+=[soup.p.string]
                    cont+=1
                    continue
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