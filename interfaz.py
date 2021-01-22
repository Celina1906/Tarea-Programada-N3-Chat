#Elaborado por: Leandro Camacho Aguilar y Celina Madrigal Murillo
#Fecha de Creación: 17/1/2021 10:43am 
#Fecha de última Modificación: 1/2/2021 9:32pm
#Versión: 3.9.0
#Importaciones
from tkinter import *
import names
import random
from tkinter import ttk
import re
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
    botonAceptar=Button(ventana1,text='Aceptar',width=18,height=2,command=aceptar1)
    botonAceptar.place(x=420,y=250)
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
def modEli():
    ventana3=Tk()
    ventana3.title('Modificar/Eliminar')
    ventana3.geometry('800x300')
    ventana3.resizable(FALSE,FALSE)
    labelTitulo1 = Label(ventana3, text = "Modificar/Eliminar contactos" , bg="Teal", fg="Azure", font = ('calibri', 40))
    labelTitulo.place(x=20,y=30)
    ventana3.configure(bg='Teal')
    labelTitulo1.place(x=40, y=20)
    radioNombre=Radiobutton(ventana3,text='Nombre',value='Hola')
    radioApellidos=Radiobutton(ventana3,text='Apellidos',value='Hola2')
    #radioNombre=Radiobutton(ventana3,text='Nombre',value='Hola')
    #radioNombre=Radiobutton(ventana3,text='Nombre',value='Hola')
    radioNombre.place(x=20,y=100)
    radioApellidos.place(x=20,y=130)
    entryDato=Entry(ventana3)
    entryDato.place(x=420,y=200)
    botonAceptar=Button(ventana3,text='Aceptar',width=18,height=2,command=lambda:print(radioNombre.value))
    botonAceptar.place(x=50,y=40)

#Botones
boton1=Button(ventanaPrincipal,text='1. Llenar BD',width=18,height=2,command=boton1Funcion)
boton2=Button(ventanaPrincipal,text='2. Insertar contacto',width=20,height=2,command=boton2Funcion)
boton3=Button(ventanaPrincipal,text='3. Modificar contacto',width=20,height=2,command=modEli)
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