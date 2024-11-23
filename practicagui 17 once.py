from tkinter import *
from tkinter import ttk
import numpy as np



def practica():
    matriz = Tk()
    matriz.geometry("700x600")
    matriz.title("INVENTARIO LOCAL")

    
            
        

    #crear notebook (pestañas)
    notebook = ttk.Notebook(matriz)
    notebook.pack(expand=True, fill="both")
    #crear las pestañas
    ingreso = Frame(notebook)
    operaciones = Frame(notebook)
    #agregar las pestañas al notebook
    notebook.add(ingreso, text="Ingresar Datos")
    notebook.add(operaciones, text="Operaciones")
    #contenido primera pestaña
    nNom = Label(ingreso, text = "Nombre Producto: ").grid(row = 0, column = 0)
    nTip = Label(ingreso, text = "Tipo de Prodcuto: ").grid(row = 1, column = 0 )
    nPrecio = Label(ingreso, text = "Valor del Producto: ").grid(row = 2, column = 0)
    nCant = Label(ingreso, text = "cantidad vendida: ").grid(row = 3, column = 0)
    nMes = Label(ingreso, text = "Ingresar Mes(ejemplo: 1, 2, 3...): ").grid(row = 4, column = 0)
    entradaMes = Entry(ingreso, width = 20)
    entradaMes.grid(row = 4, column = 1)
    entradaColum = Entry(ingreso, width = 20)
    entradaColum.grid(row = 0, column = 1)
    entradaFilas = Entry(ingreso, width = 20)
    entradaFilas.grid(row = 1, column = 1)
    entradaPrecio = Entry(ingreso, width = 20)
    entradaPrecio.grid(row = 2, column = 1)
    entradaCant = Entry(ingreso, width = 20)
    entradaCant.grid(row = 3, column = 1)
    
    #centrar primera pestaña
    ingreso.grid_columnconfigure(0, weight=1)
    ingreso.grid_columnconfigure(2, weight=1)
    ingreso.grid_columnconfigure(1, weight=0)
    #punto de impresion
    areaMatriz = Text(ingreso, height=25, width=30)
    areaMatriz.grid(row=6, column=0, columnspan=3)
    areasecond = Text(operaciones, height=30, width=60)
    areasecond.grid(row=5, column=0, columnspan=3)
    areasecond.insert(END, "Para Buscar!:\nnombre + numero del mes + buscar.\ncategoria + numero del mes + buscar.\nmes + reporte total del mes.\n--->Recuerda cumplir con los parametros establecidos<---\n")

    
    #texto en la segunda pestaña
   
    manejo = Label(operaciones, text = "SECCION INVENTARIO!!").grid(row = 0, column = 1)
    CambioColum = Label(operaciones, text = "Buscar Producto por nombre: ").grid(row = 1, column = 0)
    cambioFila = Label(operaciones, text = "Buscar Producto por Categoría: ").grid(row = 2, column = 0)
    numero = Label(operaciones, text = "Numero Del Mes: ").grid(row = 3, column = 0)
    
    #entradas segunda pestaña
    entradaPosCol = Entry(operaciones, width = 20)
    entradaPosCol.grid(row = 1, column = 1)
    entradaPosFil = Entry(operaciones, width = 20)
    entradaPosFil.grid(row = 2, column = 1)
    entradaNum = Entry(operaciones, width = 20)
    entradaNum.grid(row = 3, column = 1)
    #centrar segunda pestaña
    operaciones.grid_columnconfigure(0, weight=1)
    operaciones.grid_columnconfigure(2, weight=1)
    operaciones.grid_columnconfigure(1, weight=0)
    #botones
    botonImprimir = Button(ingreso, text = "Ingresar Venta :D")
    botonImprimir.grid(row=5, column=1)
    botonIngresar = Button(operaciones, text = "Reporte Total del Mes")
    botonIngresar.grid(row=4, column = 0)
    botonImp = Button(operaciones, text = "--->Buscar<---")
    botonImp.grid(row=4, column = 1)
  
   
        
                 
 
    
    














practica()
    
