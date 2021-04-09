#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 17/1/2021 10:43am 
#Fecha de última Modificación: 1/2/2021 9:32pm
#Versión: 3.9.0
#Importaciones
from tkinter import *
from archivos import *
import names
import random
from tkinter import ttk
import re
from ArchReqs import *
from Funciones import *
from reportes import *
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
nomArchivo='contactos'
listaFrases=[]
inicio=5
ultimo2=-1
registroChats=[]
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
    def aceptar1():
        '''
        Funcionamiento: Crea la base de datos
        Entradas: NA
        Salidas: NA
        '''
        global listaContactos
        contacto1=None
        try:
            numContactos=int(entryCantContactos.get())
            if numContactos<0 or numContactos>500:
                ventanaError=Tk()
                ventanaError.title('ERROR')
                ventanaError.geometry('750x200')
                ventanaError.resizable(FALSE,FALSE)
                labelError=Label(ventanaError,text='ERROR: Debe digitar un número mayor a 0 y menor a 500 ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                labelError.place(x=10,y=100)
                ventanaError.configure(bg='Tomato')
                ventanaError.mainloop()
            else:
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
                    for i in listaContactos:
                        while i.numero==anumero:
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
                graba(nomArchivo,listaContactos)
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
    def limpiar():
        entryCantContactos.delete(0,END)
    botonAceptar=Button(ventana1,text='Aceptar',width=18,height=2,command=aceptar1)
    botonAceptar.place(x=300,y=250)
    botonLimpiar=Button(ventana1,text='Limpiar',width=18,height=2,command=limpiar)
    botonLimpiar.place(x=460,y=250)
def boton2Funcion():
    ventana2=Tk()
    ventana2.title('Insertar contacto')
    ventana2.geometry('600x500')
    ventana2.resizable(FALSE,FALSE)
    labelTitulo1 = Label(ventana2, text = "Insertar contacto" , bg="Teal", fg="Azure", font = ('calibri', 40))
    labelTitulo.place(x=20,y=30)
    ventana2.configure(bg='Teal')
    labelTitulo1.place(x=40, y=20)
    labelNombre=Label(ventana2,text='Nombre: ', bg='Teal', font=('arial',15))  
    labelNombre.place(x=50,y=120)
    entryNombre=Entry(ventana2)
    entryNombre.place(x=210,y=120)
    labelApellidos=Label(ventana2,text='Apellidos: ',bg='Teal',font=('arial',15))
    labelApellidos.place(x=50,y=160)
    entryApellidos=Entry(ventana2)
    entryApellidos.place(x=210,y=160)
    labelTipo=Label(ventana2,text='Tipo: ',bg='Teal',font=('arial',15))
    labelTipo.place(x=50,y=200)
    comboTipo=ttk.Combobox(ventana2,values=['Celular','Laboral','Particular','Fax'])
    comboTipo.place(x=210,y=200)
    comboTipo.config(state="readonly")
    labelNumero=Label(ventana2,text='Número: ',bg='Teal',font=('arial',15))
    labelNumero.place(x=50,y=240)
    entryNumero=Entry(ventana2)
    entryNumero.place(x=210,y=240)
    labelCorreo=Label(ventana2,text='Correo: ',bg='Teal',font=('arial',15))
    labelCorreo.place(x=50,y=280)
    entryCorreo1=Entry(ventana2)
    entryCorreo1.place(x=360,y=280)
    comboCorreo1=ttk.Combobox(ventana2,values=['Particular','Laboral'])
    comboCorreo1.place(x=210,y=280)
    comboCorreo1.config(state="readonly")
    entryCorreo2=Entry(ventana2)
    entryCorreo2.place(x=360,y=320)
    comboCorreo2=ttk.Combobox(ventana2,values=['Particular','Laboral'])
    comboCorreo2.place(x=210,y=320)
    comboCorreo2.config(state="readonly")
    entryCorreo3=Entry(ventana2)
    entryCorreo3.place(x=360,y=360)
    comboCorreo3=ttk.Combobox(ventana2,values=['Particular','Laboral'])
    comboCorreo3.place(x=210,y=360)  
    def limpiar():
        entryNombre.delete(0,END)
        entryApellidos.delete(0,END)
        entryNumero.delete(0,END)
        entryCorreo1.delete(0,END)
        entryCorreo2.delete(0,END)
        entryCorreo3.delete(0,END)
        comboTipo.set('')
        comboCorreo1.set('')
        comboCorreo2.set('')
        comboCorreo3.set('')
    def ingresar():
        global listaContactos
        correo1=0
        correo2=0
        correo3=0
        aapellidos=''
        acorreos=[]
        if comboTipo.get()=='':
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('750x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: El tipo no puede ser vacío ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        if not re.match("^\d{8}$",entryNumero.get()):
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('750x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: El formato del número no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        if comboTipo.get()=='Celular' and entryNumero.get()[0]!='6'and entryNumero.get()[0]!='7'and entryNumero.get()[0]!='8'and entryNumero.get()[0]!='9':
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('750x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: El formato del número celular no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        for i in listaContactos:
            if i.numero==int(entryNumero.get()):
                ventanaError=Tk()
                ventanaError.title('ERROR')
                ventanaError.geometry('750x200')
                ventanaError.resizable(FALSE,FALSE)
                labelError=Label(ventanaError,text='ERROR: Número repetido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                labelError.place(x=10,y=100)
                ventanaError.configure(bg='Tomato')
                ventanaError.mainloop()
        if comboCorreo1.get()=='' and entryCorreo1.get()!='':
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('750x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: Debe seleccionar el tipo de correo ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        if comboCorreo1.get()!='' and entryCorreo1.get()=='':
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('750x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: El correo no puede ser vacío ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        if comboCorreo2.get()=='' and entryCorreo2.get()!='':
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('750x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: Debe seleccionar el tipo de correo ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        if comboCorreo2.get()!='' and entryCorreo2.get()=='':
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('750x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: El correo no puede ser vacío ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        if comboCorreo3.get()=='' and entryCorreo3.get()!='':
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('750x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: Debe seleccionar el tipo de correo ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        if comboCorreo3.get()!='' and entryCorreo3.get()=='':
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('750x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: El correo no puede ser vacío ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        if entryCorreo1.get()!='' and not re.match("[^@]+@[^@]+\.[^@]+",entryCorreo1.get()):
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('750x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: El formato del correo no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        if entryCorreo2.get()!='' and not re.match("[^@]+@[^@]+\.[^@]+",entryCorreo2.get()):
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('750x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: El formato del correo no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        if entryCorreo3.get()!='' and not re.match("[^@]+@[^@]+\.[^@]+",entryCorreo3.get()):
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('750x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: El formato del correo no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop()
        if comboTipo.get()=='Celular':
            atipo=1
        if comboTipo.get()=='Laboral':
            atipo=2
        if comboTipo.get()=='Particular':
            atipo=3
        if comboTipo.get()=='Fax':
            atipo=4
        if comboCorreo1.get()!=''and entryCorreo1.get()!='':
            if comboCorreo1.get()=='Particular':
                correo1=(1,entryCorreo1.get())
            else:
                correo1=(2,entryCorreo1.get())
        if comboCorreo2.get()!=''and entryCorreo2.get()!='':
            if comboCorreo2.get()=='Particular':
                correo2=(1,entryCorreo2.get())
            else:
                correo2=(2,entryCorreo2.get())
        if comboCorreo3.get()!=''and entryCorreo3.get()!='':
            if comboCorreo3.get()=='Particular':
                correo3=(1,entryCorreo3.get())
            else:
                correo3=(2,entryCorreo3.get())
        if correo1!=0:
            acorreos+=[correo1]
        if correo2!=0:
            acorreos+=[correo2]
        if correo3!=0:
            acorreos+=[correo3]
        anombre=entryNombre.get()
        nuevoContacto=Contacto(anombre)
        for i in entryApellidos.get():
            if i==' ':
               aapellidos+='-'
            else:
                aapellidos+=i
        nuevoContacto.setApellidos(aapellidos)
        nuevoContacto.setTipo(atipo)
        nuevoContacto.setNumero(int(entryNumero.get()))
        nuevoContacto.setCorreo(acorreos)
        listaContactos+=[nuevoContacto]
        graba(nomArchivo,listaContactos)
        ventanaCambio=Tk()
        ventanaCambio.title('Contacto Ingresado')
        ventanaCambio.geometry('600x300')
        ventanaCambio.resizable(FALSE,FALSE)
        labelCambio=Label(ventanaCambio,text='Contacto ingresado con éxito ', bg='Teal', font=('arial',20))
        labelCambio.place(x=50,y=150)
        ventanaCambio.configure(bg='Teal')
        ventanaCambio.mainloop()
        print (listaContactos)
        for i in listaContactos:
            print(i.nombre)
            print(i.apellidos)
            print(i.tipo)
            print(i.numero)
            print(i.correo)
            print()
    botonLimpiar=Button(ventana2,text='Limpiar',width=18,height=2,command=limpiar)
    botonLimpiar.place(x=60,y=440)    
    botonAceptar=Button(ventana2,text='Aceptar',width=18,height=2,command=ingresar)
    botonAceptar.place(x=200,y=440)

def modificar():
    global listaContactos
    ventanaMod=Tk()
    ventanaMod.config(bg='Teal')
    ventanaMod.title('Modificar contacto')
    ventanaMod.geometry('600x300')
    ventanaMod.resizable(FALSE,FALSE)
    labelTitulo=Label(ventanaMod,text='Modificar contacto', bg='Teal',fg="Azure", font=('arial',20))
    labelTitulo.place(x=150,y=50)
    labelNumero=Label(ventanaMod,text='Número del contacto: ',bg='Teal',font=('',15))
    labelNumero.place(x=120,y=130)
    entryNumero=Entry(ventanaMod)
    entryNumero.place(x=330,y=130,width=140,height=30)
    def buscarNumero():
        bandera=0
        for contac in listaContactos:
            if entryNumero.get() == str(contac.numero):
                bandera=1
                ventanaMod2=Tk()
                ventanaMod2.title('Modificar contacto')
                ventanaMod2.geometry('600x500')
                ventanaMod2.resizable(FALSE,FALSE)
                labelTitulo1 = Label(ventanaMod2, text = "Modificar contacto" , bg="Teal", fg="Azure", font = ('calibri', 40))
                labelTitulo.place(x=20,y=30)
                ventanaMod2.configure(bg='Teal')
                labelTitulo1.place(x=40, y=20)
                labelNombre=Label(ventanaMod2,text='Nombre: ', bg='Teal', font=('arial',15))  
                labelNombre.place(x=50,y=120)
                entryNombre=Entry(ventanaMod2)
                entryNombre.place(x=210,y=120)
                labelApellidos=Label(ventanaMod2,text='Apellidos: ',bg='Teal',font=('arial',15))
                labelApellidos.place(x=50,y=160)
                entryApellidos=Entry(ventanaMod2)
                entryApellidos.place(x=210,y=160)
                labelTipo=Label(ventanaMod2,text='Tipo: ',bg='Teal',font=('arial',15))
                labelTipo.place(x=50,y=200)
                comboTipo=ttk.Combobox(ventanaMod2,values=['Celular','Laboral','Particular','Fax'])
                comboTipo.place(x=210,y=200)
                comboTipo.config(state="readonly")
                labelNumero=Label(ventanaMod2,text='Número: ',bg='Teal',font=('arial',15))
                labelNumero.place(x=50,y=240)
                entryNumero2=Entry(ventanaMod2)
                entryNumero2.place(x=210,y=240)
                labelCorreo=Label(ventanaMod2,text='Correo: ',bg='Teal',font=('arial',15))
                labelCorreo.place(x=50,y=280)
                entryCorreo1=Entry(ventanaMod2)
                entryCorreo1.place(x=360,y=280)
                comboCorreo1=ttk.Combobox(ventanaMod2,values=['Particular','Laboral'])
                comboCorreo1.place(x=210,y=280)
                comboCorreo1.config(state="readonly")
                entryCorreo2=Entry(ventanaMod2)
                entryCorreo2.place(x=360,y=320)
                comboCorreo2=ttk.Combobox(ventanaMod2,values=['Particular','Laboral'])
                comboCorreo2.place(x=210,y=320)
                comboCorreo2.config(state="readonly")
                entryCorreo3=Entry(ventanaMod2)
                entryCorreo3.place(x=360,y=360)
                comboCorreo3=ttk.Combobox(ventanaMod2,values=['Particular','Laboral'])
                comboCorreo3.place(x=210,y=360)  
                def limpiar():
                    entryNombre.delete(0,END)
                    entryApellidos.delete(0,END)
                    entryNumero2.delete(0,END)
                    entryCorreo1.delete(0,END)
                    entryCorreo2.delete(0,END)
                    entryCorreo3.delete(0,END)
                    comboTipo.set('')
                    comboCorreo1.set('')
                    comboCorreo2.set('')
                    comboCorreo3.set('')
                def ingresar():
                    global listaContactos
                    correo1=0
                    correo2=0
                    correo3=0
                    aapellidos=''
                    acorreos=[]
                    if comboTipo.get()=='':
                        ventanaError=Tk()
                        ventanaError.title('ERROR')
                        ventanaError.geometry('750x200')
                        ventanaError.resizable(FALSE,FALSE)
                        labelError=Label(ventanaError,text='ERROR: El tipo no puede ser vacío ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                        labelError.place(x=10,y=100)
                        ventanaError.configure(bg='Tomato')
                        ventanaError.mainloop()
                    if not re.match("^\d{8}$",entryNumero2.get()):
                        ventanaError=Tk()
                        ventanaError.title('ERROR')
                        ventanaError.geometry('750x200')
                        ventanaError.resizable(FALSE,FALSE)
                        labelError=Label(ventanaError,text='ERROR: El formato del número no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                        labelError.place(x=10,y=100)
                        ventanaError.configure(bg='Tomato')
                        ventanaError.mainloop()
                    if comboTipo.get()=='Celular' and entryNumero.get()[0]!='6'and entryNumero.get()[0]!='7'and entryNumero.get()[0]!='8'and entryNumero.get()[0]!='9':
                        ventanaError=Tk()
                        ventanaError.title('ERROR')
                        ventanaError.geometry('750x200')
                        ventanaError.resizable(FALSE,FALSE)
                        labelError=Label(ventanaError,text='ERROR: El formato del número celular no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                        labelError.place(x=10,y=100)
                        ventanaError.configure(bg='Tomato')
                        ventanaError.mainloop()
                    for i in listaContactos:
                        if i.numero==int(entryNumero2.get()):
                            ventanaError=Tk()
                            ventanaError.title('ERROR')
                            ventanaError.geometry('750x200')
                            ventanaError.resizable(FALSE,FALSE)
                            labelError=Label(ventanaError,text='ERROR: Número repetido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                            labelError.place(x=10,y=100)
                            ventanaError.configure(bg='Tomato')
                            ventanaError.mainloop()
                    if comboCorreo1.get()=='' and entryCorreo1.get()!='':
                        ventanaError=Tk()
                        ventanaError.title('ERROR')
                        ventanaError.geometry('750x200')
                        ventanaError.resizable(FALSE,FALSE)
                        labelError=Label(ventanaError,text='ERROR: Debe seleccionar el tipo de correo ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                        labelError.place(x=10,y=100)
                        ventanaError.configure(bg='Tomato')
                        ventanaError.mainloop()
                    if comboCorreo1.get()!='' and entryCorreo1.get()=='':
                        ventanaError=Tk()
                        ventanaError.title('ERROR')
                        ventanaError.geometry('750x200')
                        ventanaError.resizable(FALSE,FALSE)
                        labelError=Label(ventanaError,text='ERROR: El correo no puede ser vacío ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                        labelError.place(x=10,y=100)
                        ventanaError.configure(bg='Tomato')
                        ventanaError.mainloop()
                    if comboCorreo2.get()=='' and entryCorreo2.get()!='':
                        ventanaError=Tk()
                        ventanaError.title('ERROR')
                        ventanaError.geometry('750x200')
                        ventanaError.resizable(FALSE,FALSE)
                        labelError=Label(ventanaError,text='ERROR: Debe seleccionar el tipo de correo ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                        labelError.place(x=10,y=100)
                        ventanaError.configure(bg='Tomato')
                        ventanaError.mainloop()
                    if comboCorreo2.get()!='' and entryCorreo2.get()=='':
                        ventanaError=Tk()
                        ventanaError.title('ERROR')
                        ventanaError.geometry('750x200')
                        ventanaError.resizable(FALSE,FALSE)
                        labelError=Label(ventanaError,text='ERROR: El correo no puede ser vacío ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                        labelError.place(x=10,y=100)
                        ventanaError.configure(bg='Tomato')
                        ventanaError.mainloop()
                    if comboCorreo3.get()=='' and entryCorreo3.get()!='':
                        ventanaError=Tk()
                        ventanaError.title('ERROR')
                        ventanaError.geometry('750x200')
                        ventanaError.resizable(FALSE,FALSE)
                        labelError=Label(ventanaError,text='ERROR: Debe seleccionar el tipo de correo ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                        labelError.place(x=10,y=100)
                        ventanaError.configure(bg='Tomato')
                        ventanaError.mainloop()
                    if comboCorreo3.get()!='' and entryCorreo3.get()=='':
                        ventanaError=Tk()
                        ventanaError.title('ERROR')
                        ventanaError.geometry('750x200')
                        ventanaError.resizable(FALSE,FALSE)
                        labelError=Label(ventanaError,text='ERROR: El correo no puede ser vacío ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                        labelError.place(x=10,y=100)
                        ventanaError.configure(bg='Tomato')
                        ventanaError.mainloop()
                    if entryCorreo1.get()!='' and not re.match("[^@]+@[^@]+\.[^@]+",entryCorreo1.get()):
                        ventanaError=Tk()
                        ventanaError.title('ERROR')
                        ventanaError.geometry('750x200')
                        ventanaError.resizable(FALSE,FALSE)
                        labelError=Label(ventanaError,text='ERROR: El formato del correo no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                        labelError.place(x=10,y=100)
                        ventanaError.configure(bg='Tomato')
                        ventanaError.mainloop()
                    if entryCorreo2.get()!='' and not re.match("[^@]+@[^@]+\.[^@]+",entryCorreo2.get()):
                        ventanaError=Tk()
                        ventanaError.title('ERROR')
                        ventanaError.geometry('750x200')
                        ventanaError.resizable(FALSE,FALSE)
                        labelError=Label(ventanaError,text='ERROR: El formato del correo no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                        labelError.place(x=10,y=100)
                        ventanaError.configure(bg='Tomato')
                        ventanaError.mainloop()
                    if entryCorreo3.get()!='' and not re.match("[^@]+@[^@]+\.[^@]+",entryCorreo3.get()):
                        ventanaError=Tk()
                        ventanaError.title('ERROR')
                        ventanaError.geometry('750x200')
                        ventanaError.resizable(FALSE,FALSE)
                        labelError=Label(ventanaError,text='ERROR: El formato del correo no es válido ', bg='Tomato',fg='AliceBlue', font=('arial',20))
                        labelError.place(x=10,y=100)
                        ventanaError.configure(bg='Tomato')
                        ventanaError.mainloop()
                    if comboTipo.get()=='Celular':
                        atipo=1
                    if comboTipo.get()=='Laboral':
                        atipo=2
                    if comboTipo.get()=='Particular':
                        atipo=3
                    if comboTipo.get()=='Fax':
                        atipo=4
                    if comboCorreo1.get()!=''and entryCorreo1.get()!='':
                        if comboCorreo1.get()=='Particular':
                            correo1=(1,entryCorreo1.get())
                        else:
                            correo1=(2,entryCorreo1.get())
                    if comboCorreo2.get()!=''and entryCorreo2.get()!='':
                        if comboCorreo2.get()=='Particular':
                            correo2=(1,entryCorreo2.get())
                        else:
                            correo2=(2,entryCorreo2.get())
                    if comboCorreo3.get()!=''and entryCorreo3.get()!='':
                        if comboCorreo3.get()=='Particular':
                            correo3=(1,entryCorreo3.get())
                        else:
                            correo3=(2,entryCorreo3.get())
                    if correo1!=0:
                        acorreos+=[correo1]
                    if correo2!=0:
                        acorreos+=[correo2]
                    if correo3!=0:
                        acorreos+=[correo3]
                    anombre=entryNombre.get()
                    
                    for i in entryApellidos.get():
                        if i==' ':
                            aapellidos+='-'
                        else:
                            aapellidos+=i
                    contac.nombre=anombre
                    contac.apellidos=aapellidos
                    contac.tipo=atipo
                    contac.numero=int(entryNumero2.get())
                    contac.correo=acorreos
                    graba(nomArchivo,listaContactos)
                    ventanaCambio=Tk()
                    ventanaCambio.title('Contacto modificado con exito')
                    ventanaCambio.geometry('600x300')
                    ventanaCambio.resizable(FALSE,FALSE)
                    labelCambio=Label(ventanaCambio,text='Contacto modificado con éxito ', bg='Teal', font=('arial',20))
                    labelCambio.place(x=50,y=150)
                    ventanaCambio.configure(bg='Teal')
                    ventanaCambio.mainloop()
                    print (listaContactos)
                    for i in listaContactos:
                        print(i.nombre)
                        print(i.apellidos)
                        print(i.tipo)
                        print(i.numero)
                        print(i.correo)
                        print()
                botonLimpiar=Button(ventanaMod2,text='Limpiar',width=18,height=2,command=limpiar)
                botonLimpiar.place(x=60,y=440)    
                botonAceptar=Button(ventanaMod2,text='Aceptar',width=18,height=2,command=ingresar)
                botonAceptar.place(x=200,y=440)
        if bandera==0:
            ventanaCambio=Tk()
            ventanaCambio.title('No se encontró el contacto')
            ventanaCambio.geometry('600x300')
            ventanaCambio.resizable(FALSE,FALSE)
            labelCambio=Label(ventanaCambio,text='No se encontró un contacto con ese número', bg='Teal', font=('arial',20))
            labelCambio.place(x=50,y=150)
            ventanaCambio.configure(bg='Teal')
            ventanaCambio.mainloop()
    botonAceptar=Button(ventanaMod,text='Aceptar',width=18,height=2,command=buscarNumero)
    botonAceptar.place(x=200,y=200)
   
def eliminar():
    global listaContactos
    ventanaMod=Tk()
    ventanaMod.config(bg='Teal')
    ventanaMod.title('Eliminar contacto')
    ventanaMod.geometry('600x300')
    ventanaMod.resizable(FALSE,FALSE)
    labelTitulo=Label(ventanaMod,text='Eliminar contacto', bg='Teal',fg="Azure", font=('arial',20))
    labelTitulo.place(x=150,y=50)
    labelNumero=Label(ventanaMod,text='Número del contacto: ',bg='Teal',font=('',15))
    labelNumero.place(x=120,y=130)
    entryNumero=Entry(ventanaMod)
    entryNumero.place(x=330,y=130,width=140,height=30)
    def buscarNumero():
        bandera=0
        for contac in listaContactos:
            if entryNumero.get() == str(contac.numero):
                bandera=1
                listaContactos.remove(contac)
                graba(nomArchivo,listaContactos)
                ventanaCambio=Tk()
                ventanaCambio.title('Contacto eliminado')
                ventanaCambio.geometry('600x300')
                ventanaCambio.resizable(FALSE,FALSE)
                labelCambio=Label(ventanaCambio,text='Contacto eliminado con éxito', bg='Teal', font=('arial',20))
                labelCambio.place(x=50,y=150)
                ventanaCambio.configure(bg='Teal')
                ventanaCambio.mainloop()
        if bandera==0:
            ventanaCambio=Tk()
            ventanaCambio.title('No se encontró el contacto')
            ventanaCambio.geometry('600x300')
            ventanaCambio.resizable(FALSE,FALSE)
            labelCambio=Label(ventanaCambio,text='No se encontró un contacto con ese número', bg='Teal', font=('arial',20))
            labelCambio.place(x=50,y=150)
            ventanaCambio.configure(bg='Teal')
            ventanaCambio.mainloop()
    botonAceptar=Button(ventanaMod,text='Aceptar',width=18,height=2,command=buscarNumero)
    botonAceptar.place(x=200,y=200)
    ventanaMod.mainloop()
   
def modEli():
    ventana3=Toplevel()
    ventana3.title('Modificar/Eliminar')
    ventana3.geometry('800x300')
    ventana3.resizable(FALSE,FALSE)
    labelTitulo1 = Label(ventana3, text = "Modificar/Eliminar contactos" , bg="Teal", fg="Azure", font = ('calibri', 40))
    labelTitulo.place(x=20,y=30)
    ventana3.configure(bg='Teal')
    labelTitulo1.place(x=40, y=20)
    entryDato=Entry(ventana3)
    entryDato.place(x=270,y=150)
    valor = IntVar()
    def aceptar():
        global listaContactos
        bandera=0
        nuevaLista=[]
        x=valor.get()
        if x==0 or entryDato.get()=='':
            bandera=1
            ventanaError=Tk()
            ventanaError.title('ERROR')
            ventanaError.geometry('750x200')
            ventanaError.resizable(FALSE,FALSE)
            labelError=Label(ventanaError,text='ERROR: Debe llenar los espacios vacíos', bg='Tomato',fg='AliceBlue', font=('arial',20))
            labelError.place(x=10,y=100)
            ventanaError.configure(bg='Tomato')
            ventanaError.mainloop() 
        elif x==1:
            for contac in listaContactos:
                if entryDato.get() in contac.nombre:
                    nuevaLista+=[contac]
        elif x==2: 
            for contac in listaContactos:
                if entryDato.get() in contac.apellidos:
                    nuevaLista+=[contac]
        elif x==3:
            bandera2=0
            try: 
                int(entryDato.get())
                bandera2=1
            except:
                ventanaError=Tk()
                ventanaError.title('ERROR')
                ventanaError.geometry('750x200')
                ventanaError.resizable(FALSE,FALSE)
                labelError=Label(ventanaError,text='ERROR: Dato digitado no válido', bg='Tomato',fg='AliceBlue', font=('arial',20))
                labelError.place(x=10,y=100)
                ventanaError.configure(bg='Tomato')
                ventanaError.mainloop() 
            if bandera2==1:
                for contac in listaContactos:
                    if entryDato.get() in str(contac.numero):
                        nuevaLista+=[contac]
        if bandera==0:
            ventana3=Tk()
            ventana3.title('Resultados')
            ventana3.geometry('800x500')
            ventana3.configure(bg='Teal')
            ventana3.resizable(FALSE,FALSE)
            labelTitulo1 = Label(ventana3, text = "Resultados de la búsqueda" , bg="Teal", fg="Azure", font = ('calibri', 25))
            labelTitulo1.place(x=40, y=20)
            labelCantidad=Label(ventana3, text = "Cantidad: " , bg="Teal", fg="Azure", font = ('calibri', 15))
            labelCantidad.place(x=500,y=20)
            entryCantidad=Entry(ventana3)
            entryCantidad.insert(0,len(nuevaLista))
            entryCantidad.config(state='readonly')
            entryCantidad.place(x=600,y=20)
            tabla=ttk.Treeview(ventana3)
            tabla['columns']=('Número','Nombre','Apellidos')
            tabla.column('#0',width=0,minwidth=0)
            tabla.column('Número',width=120,minwidth=25)
            tabla.column('Nombre',anchor=CENTER,width=120) 
            tabla.column('Apellidos',anchor=W,width=120)
            tabla.heading('#0',text='',anchor=W)
            tabla.heading('Número',text='Número',anchor=W)
            tabla.heading('Nombre',text='Nombre',anchor=CENTER)      
            tabla.heading('Apellidos',text='Apellidos',anchor=W)
            id=0 
            if len(nuevaLista)>5:
                for con in nuevaLista[0:5]:
                    tabla.insert(parent='',index='end',iid=id,text='',values=(con.numero,con.nombre,con.apellidos))
                    id+=1
            else:
                for con in nuevaLista:
                    tabla.insert(parent='',index='end',iid=id,text='',values=(con.numero,con.nombre,con.apellidos))
                    id+=1
            def flechaA():
                global inicio
                tabla2=ttk.Treeview(ventana3)
                tabla2['columns']=('Número','Nombre','Apellidos')
                tabla2.column('#0',width=0,minwidth=0)
                tabla2.column('Número',width=120,minwidth=25)
                tabla2.column('Nombre',anchor=CENTER,width=120) 
                tabla2.column('Apellidos',anchor=W,width=120)
                tabla2.heading('#0',text='',anchor=W)
                tabla2.heading('Número',text='Número',anchor=W)
                tabla2.heading('Nombre',text='Nombre',anchor=CENTER)      
                tabla2.heading('Apellidos',text='Apellidos',anchor=W)
                id=0
                fin=len(nuevaLista)
                if inicio+5>=len(nuevaLista):
                    for con in nuevaLista[inicio:len(nuevaLista)]:
                        tabla2.insert(parent='',index='end',iid=id,text='',values=(con.numero,con.nombre,con.apellidos))
                        id+=1
                        #flechaAboton['state']=DISABLED
                else:
                    for con in nuevaLista[inicio:inicio+5]:
                        tabla2.insert(parent='',index='end',iid=id,text='',values=(con.numero,con.nombre,con.apellidos))
                        id+=1
                    inicio+=5
                tabla2.place(x=100,y=200)
            def flechaB():
                flechaAboton['state']=NORMAL
                tabla2=ttk.Treeview(ventana3)
                tabla2['columns']=('Número','Nombre','Apellidos')
                tabla2.column('#0',width=0,minwidth=0)
                tabla2.column('Número',width=120,minwidth=25)
                tabla2.column('Nombre',anchor=CENTER,width=120) 
                tabla2.column('Apellidos',anchor=W,width=120)
                tabla2.heading('#0',text='',anchor=W)
                tabla2.heading('Número',text='Número',anchor=W)
                tabla2.heading('Nombre',text='Nombre',anchor=CENTER)      
                tabla2.heading('Apellidos',text='Apellidos',anchor=W)
                id=0
                ultimo=len(nuevaLista)-1
                for con in nuevaLista[ultimo-5:ultimo]:
                    tabla2.insert(parent='',index='end',iid=id,text='',values=(con.numero,con.nombre,con.apellidos))
                    id+=1
                    ultimo-=4
                #flechaBboton['state']=DISABLED
                tabla2.place(x=100,y=200)
            flechaAboton=Button(ventana3,text='--->',width=18,height=2,command=flechaA)
            flechaAboton.place(x=400,y=450)
            flechaBboton=Button(ventana3,text='<---',width=18,height=2,command=flechaB)
            flechaBboton.place(x=200,y=450)
            if len(nuevaLista)<=5:
                flechaAboton['state']=DISABLED
                flechaBboton['state']=DISABLED
            tabla.place(x=100,y=200)
            botonModificar=Button(ventana3,text='Modificar',width=20,height=2,command=modificar)
            botonModificar.place(x=200,y=120)
            botonEliminar=Button(ventana3,text='Eliminar',width=20,height=2,command=eliminar)
            botonEliminar.place(x=400,y=120)
    radioNombre = Radiobutton(ventana3, text = "Nombre", value = 1, variable = valor)
    radioNombre.place(x = 50, y = 90)
    radioApellidos = Radiobutton(ventana3, text = "Apellidos", value = 2, variable = valor)
    radioApellidos.place(x = 50, y = 120)
    radioNumero = Radiobutton(ventana3, text = "Número", value = 3, variable = valor)
    radioNumero.place(x = 50, y = 150)
    botonAceptar=Button(ventana3,text='Aceptar',width=18,height=2,command=aceptar)
    botonAceptar.place(x=370,y=250)

def boton5Funcion():
    try:
        grabarXml('contactosXML',listaContactos)
        ventanaCambio=Tk()
        ventanaCambio.title('Archivo generado')
        ventanaCambio.geometry('600x300')
        ventanaCambio.resizable(FALSE,FALSE)
        labelCambio=Label(ventanaCambio,text='Archivo generado con éxito ', bg='Teal', font=('arial',20))
        labelCambio.place(x=50,y=150)
        ventanaCambio.configure(bg='Teal')
        ventanaCambio.mainloop()
    except:
        ventanaError=Tk()
        ventanaError.title('ERROR')
        ventanaError.geometry('750x200')
        ventanaError.resizable(FALSE,FALSE)
        labelError=Label(ventanaError,text='ERROR: Ha ocurrido un error al generar el archivo', bg='Tomato',fg='AliceBlue', font=('arial',20))
        labelError.place(x=10,y=100)
        ventanaError.configure(bg='Tomato')
        ventanaError.mainloop() 
def boton6Funcion():
    global listaFrases
    try: 
        listaFrases=obtenerFrases()
        ventanaCambio=Tk()
        ventanaCambio.title('Frases obtenidas')
        ventanaCambio.geometry('600x300')
        ventanaCambio.resizable(FALSE,FALSE)
        labelCambio=Label(ventanaCambio,text='Frases obtenidas con éxito ', bg='Teal', font=('arial',20))
        labelCambio.place(x=50,y=150)
        ventanaCambio.configure(bg='Teal')
        ventanaCambio.mainloop()
    except:
        ventanaError=Tk()
        ventanaError.title('ERROR')
        ventanaError.geometry('750x200')
        ventanaError.resizable(FALSE,FALSE)
        labelError=Label(ventanaError,text='ERROR: Ha ocurrido un error al obtener las frases', bg='Tomato',fg='AliceBlue', font=('arial',20))
        labelError.place(x=10,y=100)
        ventanaError.configure(bg='Tomato')
        ventanaError.mainloop() 
def boton7Funcion():
    global listaFrases
    global listaContactos
    global registroChats
    ventanaMod=Tk()
    ventanaMod.config(bg='Teal')
    ventanaMod.title('Cantidad de chat')
    ventanaMod.geometry('600x300')
    ventanaMod.resizable(FALSE,FALSE)
    labelTitulo=Label(ventanaMod,text='Cantidad de chats', bg='Teal',fg="Azure", font=('arial',20))
    labelTitulo.place(x=150,y=50)
    entryNumero=Entry(ventanaMod)
    entryNumero.place(x=180,y=130,width=140,height=30)
    def aceptar():
        global listaFrases
        global listaContactos
        global registroChats
        nChats=int(entryNumero.get())
        while nChats!=0:
            try:
                nRandom=random.randrange(1,40)
                Ulam=[nRandom] + sucesionUlam(nRandom)
                nombreTxt="Chat"+str(nChats)
                contactosChat=buscarPersonas(listaContactos)
                registroChats+=[(contactosChat,nChats)]
                grabarChats(nombreTxt,Ulam,listaFrases,contactosChat)
                nChats-=1
            except:
                ventanaError=Tk()
                ventanaError.title('ERROR')
                ventanaError.geometry('750x200')
                ventanaError.resizable(FALSE,FALSE)
                labelError=Label(ventanaError,text='ERROR: Debe ingresar unicamente numeros.', bg='Tomato',fg='AliceBlue', font=('arial',20))
                labelError.place(x=10,y=100)
                ventanaError.configure(bg='Tomato')
                ventanaError.mainloop() 
    botonAceptar=Button(ventanaMod,text='Aceptar',width=18,height=2,command=aceptar)
    botonAceptar.place(x=370,y=250)
    def limpiar():
        entryNumero.delete(0,END)
    botonLimpiar=Button(ventanaMod,text='Limpiar',width=18,height=2,command=limpiar)
    botonLimpiar.place(x=100,y=250)
def boton8Funcion():
    ventanaReportes=Tk()
    ventanaReportes.title('Chat')
    ventanaReportes.geometry('800x400')
    ventanaReportes.resizable(FALSE,FALSE)
    ventanaReportes.configure(bg='Teal')
    labelTitulo = Label(ventanaReportes, text = "Reportes" , bg="Teal", fg="Azure", font = ('calibri', 40))
    labelTitulo.place(x=20,y=30)
    boton1=Button(ventanaReportes,text='Reporte 1',width=18,height=2,command=lambda:reporte1(listaContactos))
    boton2=Button(ventanaReportes,text='Reporte 2',width=20,height=2,command=boton2Funcion)
    boton3=Button(ventanaReportes,text='Reporte 3',width=20,height=2,command=modEli)
    boton4=Button(ventanaReportes,text='Reporte 4',width=16,height=2,command=modEli)
    boton5=Button(ventanaReportes,text='Reporte 5',width=18,height=2,command=boton5Funcion)
    boton6=Button(ventanaReportes,text='Reporte 6',width=18,height=2,command=boton6Funcion)
    boton1.place(x=25,y=120)
    boton2.place(x=175,y=120)
    boton3.place(x=340,y=120)
    boton4.place(x=510,y=120)
    boton5.place(x=650,y=120)
    boton6.place(x=100,y=200)
labelTitulo = Label(ventanaPrincipal, text = "Chat" , bg="Teal", fg="Azure", font = ('calibri', 40))
labelTitulo.place(x=20,y=30)
def boton10Funcion():
    ventanaCambio=Tk()
    ventanaCambio.title('Acerca de ')
    ventanaCambio.geometry('600x300')
    ventanaCambio.resizable(FALSE,FALSE)
    labelCambio=Label(ventanaCambio,text='Acerca de', bg='Teal', font=('arial',20))
    labelCambio.place(x=50,y=100)
    labelNombre=Label(ventanaCambio,text='Sistema de informacion: Chat', bg='Teal', font=('arial',12))
    labelNombre.place(x=50,y=130)
    labelVersion=Label(ventanaCambio,text='Versión: 1', bg='Teal', font=('arial',12))
    labelVersion.place(x=50,y=150)
    labelFecha=Label(ventanaCambio,text='Fecha de creación: 17 de enero del 2021', bg='Teal', font=('arial',12))
    labelFecha.place(x=50,y=170)
    labelAutores=Label(ventanaCambio,text='Autores: Leandro Camacho Aguilar y Celina Madrigal Murillo', bg='Teal', font=('arial',12))
    labelAutores.place(x=50,y=190)
    ventanaCambio.configure(bg='Teal')
    ventanaCambio.mainloop()

#Botones
boton1=Button(ventanaPrincipal,text='1. Llenar BD',width=18,height=2,command=boton1Funcion)
boton2=Button(ventanaPrincipal,text='2. Insertar contacto',width=20,height=2,command=boton2Funcion)
boton3=Button(ventanaPrincipal,text='3. Modificar contacto',width=20,height=2,command=modEli)
boton4=Button(ventanaPrincipal,text='4. Eliminar contacto',width=16,height=2,command=modEli)
boton5=Button(ventanaPrincipal,text='5. Exportar BD a XML',width=18,height=2,command=boton5Funcion)
boton6=Button(ventanaPrincipal,text='6. Extraer frases célebres',width=18,height=2,command=boton6Funcion)
boton7=Button(ventanaPrincipal,text='7. Chatear',width=25,height=2,command=boton7Funcion)
boton8=Button(ventanaPrincipal,text='8. Reportes',width=13,height=2,command=boton8Funcion)
boton9=Button(ventanaPrincipal,text='9. Ayuda',width=13,height=2)
boton10=Button(ventanaPrincipal,text='10. Acerca de',width=13,height=2,command=boton10Funcion)
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

#hola djmkflnmsdjflhnsdfkjsdfkljwoiueraslkjalksjd