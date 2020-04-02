import tkinter as tk
from tkinter.messagebox import showinfo
from tkinter import Tk, Label, PhotoImage, BOTTOM, TOP, LEFT, RIGHT, RIDGE

class Interfaz_Temp:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("Conversor de Temperatura")

        # Cuadro de texto
        self.label_Temp=tk.Label(self.ventana, text="Temperatura:")
        self.label_Temp.grid(column=0, row=0)
        self.dato_Temp=tk.StringVar()
        self.entry=tk.Entry(self.ventana, width=10, textvariable=self.dato_Temp)
        self.entry.grid(column=1, row=0)

        # Radio buttons
        self.Rseleccion=tk.IntVar()
        self.Rseleccion.set(3)
        self.radio1=tk.Radiobutton(self.ventana,text="Kelvin", variable=self.Rseleccion, value=1)
        self.radio1.grid(column=0, row=1) 
        self.radio2=tk.Radiobutton(self.ventana,text="Celsius", variable=self.Rseleccion, value=2)
        self.radio2.grid(column=1, row=1) 
        self.radio3=tk.Radiobutton(self.ventana,text="Fahrenheit", variable=self.Rseleccion, value=3)
        self.radio3.grid(column=2, row=1) 

        #Boton Convertir
        self.boton=tk.Button(self.ventana, text="Convertir a", command=self.conversion)
        self.boton.grid(column=1, row=2) 

        #Check Buttons
        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana,text="Kelvin", variable=self.seleccion1)
        self.check1.grid(column=0, row=3)
        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana,text="Celsius", variable=self.seleccion2)
        self.check2.grid(column=1, row=3)
        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.ventana,text="Fahrenheit", variable=self.seleccion3)
        self.check3.grid(column=2, row=3)

        # Resultados
        self.label_Kelvin=tk.Label(self.ventana, text="Kelvin:")
        self.label_Kelvin.grid(column=0, row=4)
        self.label_Celsius=tk.Label(self.ventana, text="Celsius:")
        self.label_Celsius.grid(column=0, row=5)
        self.label_Fahrenheit=tk.Label(self.ventana, text="Fahrenheit:")
        self.label_Fahrenheit.grid(column=0, row=6)

        self.kelvin_da=tk.StringVar()
        self.celsius_da=tk.StringVar()
        self.fahrenheit_da=tk.StringVar()
        self.label_Kelvin_R=tk.Label(self.ventana, text="")
        self.label_Kelvin_R.grid(column=1, row=4)
        self.label_Celsius_R=tk.Label(self.ventana, text="")
        self.label_Celsius_R.grid(column=1, row=5)
        self.label_Fahrenheit_R=tk.Label(self.ventana, text="")
        self.label_Fahrenheit_R.grid(column=1, row=6)

        self.ventana.mainloop()


    def conversion(self):
        valor=float(self.dato_Temp.get())
        if self.Rseleccion.get()==1:
            if self.seleccion1.get()==1:
                self.kelvin_da=valor
            if self.seleccion2.get()==1:
                self.celsius_da=valor-273.15
            if self.seleccion3.get()==1:
                self.fahrenheit_da=(9*(valor-273.15))/5+32

        if self.Rseleccion.get()==2:
            if self.seleccion1.get()==1:
                self.kelvin_da=valor+273.15
            if self.seleccion2.get()==1:
                self.celsius_da=valor
            if self.seleccion3.get()==1:
                self.fahrenheit_da=9*valor/5+32 

        if self.Rseleccion.get()==3:
            if self.seleccion1.get()==1:
                self.kelvin_da=(5/9)*(valor-32)+273
            if self.seleccion2.get()==1:
                self.celsius_da=(5/9)*(valor-32)
            if self.seleccion3.get()==1:
                self.fahrenheit_da=valor
        
        if self.seleccion1.get()==0:
            self.kelvin_da=""
        if self.seleccion2.get()==0:
            self.celsius_da=""
        if self.seleccion3.get()==0:
            self.fahrenheit_da=""

        self.label_Kelvin_R.configure(text=self.kelvin_da)
        self.label_Celsius_R.configure(text=self.celsius_da)
        self.label_Fahrenheit_R.configure(text=self.fahrenheit_da)

conversor_temp=Interfaz_Temp()