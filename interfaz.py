#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 17/1/2021 10:43am 
#Fecha de última Modificación: 1/2/2021 9:32pm
#Versión: 3.9.0
#Importaciones
from tkinter import *
import names
import random
#Clase Contacto
class Contacto:
    nombre=''
    apellidos=''
    tipo=0
    numero=0
    correo=[]
    def __init__(self,anombre):
        self.nombre=anombre
        self.apellidos=''
        self.tipo=0
        self.numero=0
        self.correo=[]
    def setApellidos(self,aapellidos):
        self.apellidos=aapellidos
    def getApellidos(self):
        return self.apellidos
    def setTipo(self,atipo):
        self.tipo=atipo
    def getTipo(self):
        return self.tipo
    def setNumero(self,anumero):
        self.numero=anumero
    def getNumero(self):
        return self.numero
    def setCorreo(self,acorreo):
        self.correo=acorreo
    def getCorreo(self):
        return self.correo
#Variables globales
listaContactos=[]
#Ventana Principal
ventanaPrincipal=Tk()
ventanaPrincipal.title('Chat')
ventanaPrincipal.geometry('800x400')
ventanaPrincipal.resizable(FALSE,FALSE)
ventanaPrincipal.configure(bg='Teal')
labelTitulo = Label(ventanaPrincipal, text = "Chat" , bg="Teal", fg="Azure", font = ('calibri', 40))
labelTitulo.place(x=20,y=30)
#Funciones Botones
#Boton 1
def boton1Funcion():
    '''
    Funcionamiento: Crea la ventana del primer botón
    Entradas: NA
    Salidas: NA
    '''
    ventana1=Tk()
    ventana1.title('Llenar BD')
    ventana1.geometry('800x300')
    ventana1.resizable(FALSE,FALSE)
    labelTitulo1 = Label(ventana1, text = "Llenar BD" , bg="Teal", fg="Azure", font = ('calibri', 40))
    labelTitulo.place(x=20,y=30)
    ventana1.configure(bg='Teal')
    labelTitulo1.place(x=40, y=20)
    labelContactos=Label(ventana1,text='Digite la cantidad de contactos a realizar de forma automática ', bg='Teal', font=('arial',15))  
    labelContactos.place(x=50,y=120)
    entryCantContactos=Entry(ventana1)
    entryCantContactos.place(x=420,y=200)
    def aceptar():
        global listaContactos
        contacto1=None
        try:
            numContactos=int(entryCantContactos.get())
            while numContactos!=0:
                acorreo=[]
                anombre=names.get_first_name()
                contacto1=Contacto(anombre)
                aapellidos=names.get_last_name()+'-'+names.get_last_name()
                contacto1.setApellidos(aapellidos)
                tipo=[1,2,3,4]
                atipo=random.choice(tipo)
                contacto1.setTipo(atipo)
                if atipo==1:
                    anumero=random.randint(60000000,99999999)
                else:
                    anumero=random.randint(10000000,99999999)
                contacto1.setNumero(anumero)
                cantCorreos=[0,1,2,3]
                cantCorreos=random.choice(cantCorreos)
                while cantCorreos!=0:
                    tipoCorreo=[1,2]
                    acorreo+=[(random.choice(tipoCorreo),anombre.lower()+str(cantCorreos)+'@gmail.com')]
                    cantCorreos-=1
                contacto1.setCorreo(acorreo)
                listaContactos+=[contacto1]
                numContactos-=1
            ventanaCambio=Tk()
            ventanaCambio.title('Base de datos creada')
            ventanaCambio.geometry('600x300')
            ventanaCambio.resizable(FALSE,FALSE)
            labelCambio=Label(ventanaCambio,text='Base de datos creada con éxito ', bg='Teal', font=('arial',20))
            labelCambio.place(x=50,y=150)
            ventanaCambio.configure(bg='Teal')
            ventanaCambio.mainloop()
        except:
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('600x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: Dato ingresado no válido ', bg='Tomato', fg='AliceBlue', font=('arial',20))
            labelError.place(x=50,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
    botonAceptar=Button(ventana1,text='Aceptar',width=18,height=2,command=aceptar)
    botonAceptar.place(x=420,y=250)
#Botones
boton1=Button(ventanaPrincipal,text='1. Llenar BD',width=18,height=2,command=boton1Funcion)
boton2=Button(ventanaPrincipal,text='2. Insertar contacto',width=20,height=2)
boton3=Button(ventanaPrincipal,text='3. Modificar contacto',width=20,height=2)
boton4=Button(ventanaPrincipal,text='4. Eliminar contacto',width=16,height=2)
boton5=Button(ventanaPrincipal,text='5. Exportar BD a XML',width=18,height=2)
boton6=Button(ventanaPrincipal,text='6. Extraer frases célebres',width=18,height=2)
boton7=Button(ventanaPrincipal,text='7. Chatear',width=25,height=2)
boton8=Button(ventanaPrincipal,text='8. Reportes',width=13,height=2)
boton9=Button(ventanaPrincipal,text='9. Ayuda',width=13,height=2)
boton10=Button(ventanaPrincipal,text='10. Acerca de',width=13,height=2)
boton11=Button(ventanaPrincipal,text='11. Salir',width=10,height=2,command= lambda:ventanaPrincipal.destroy())
#Colocación de botones de pantalla principal
boton1.place(x=25,y=120)
boton2.place(x=175,y=120)
boton3.place(x=340,y=120)
boton4.place(x=510,y=120)
boton5.place(x=650,y=120)
boton6.place(x=100,y=200)
boton7.place(x=260,y=200)
boton8.place(x=470,y=200)
boton9.place(x=600,y=200)
boton10.place(x=300,y=280)
boton11.place(x=450,y=280)
ventanaPrincipal.mainloop()