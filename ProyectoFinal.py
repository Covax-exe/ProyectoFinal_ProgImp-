from tkinter import *
from tkinter import ttk
import numpy as np

nombre = np.array([[None]*12]*50)
tipo = np.array([[None]*12]*50)
valor = np.zeros((12,50))
cantidad = np.zeros((12,50))
cont = [0] * 12



# ------------ FUNCIÓN BOTONES ----------------
def ingresarVenta():
    if (((len(entradaMes.get().strip()) !=0 ) and (((int(entradaMes.get().strip()))>0) and ((int(entradaMes.get().strip()))<13))) and (len(entradaColum.get().strip())!=0) and (len(entradaFilas.get().strip()) != 0) and ((len(entradaPrecio.get().strip()) != 0) and ((float(entradaPrecio.get().strip())) >0)) and ((len(entradaCant.get().strip())!=0) and ((int(entradaCant.get().strip()))>0 ))):
        nombrex = entradaColum.get().strip()
        tipox = entradaFilas.get().strip()
        valorx = float(entradaPrecio.get().strip())
        cantidadx = int(entradaCant.get().strip())
        mesx = int(entradaMes.get().strip())
        x = mesx - 1
        p = 0
        for j in range (0,(cont[x]+1),1):
            if ((nombrex.upper() == nombre[x][j]) and (tipox.upper() == tipo[mesx-1][j])):
                cantidad[x][j]= cantidad[x][j] +cantidadx
                p=1
                result ="\nSe agregó la cantidad vendida al producto: " + nombre[mesx-1][j]
                areaMatriz.insert(END, result)
        if (p==0):
            nombre[x][cont[x]]= nombrex.upper()
            tipo[x][cont[x]]= tipox.upper()
            valor[x][cont[x]]= valorx
            cantidad[x][cont[x]]= cantidadx
            cont[x] = cont[x] + 1
            areaMatriz.insert(END, "\nSe agregó un nuevo producto")
    else:
        areaMatriz.insert(END, "\nINGRESO INVÁLIDO")


def reporteTotalMes():
    mes= int(entradaNum.get().strip())

    if 1 <= mes and mes <= 12:
        x = mes - 1 # para que coincida con la matriz
        total_ventas = 0
        total_valor = 0
        areasecond.delete("1.0", END)
        for i in range(cont[x]):
            total_ventas += cantidad[x][i]
            total_valor += cantidad[x][i] * valor[x][i]
            producto_info = f"Producto: {nombre[x][i]}, Tipo: {tipo[x][i]} \nCantidad: {cantidad[x][i]}, Valor Unitario: {valor[x][i]}\n"
            areasecond.insert(END, producto_info)
        resumen = f"\nTotal de ventas en el mes {mes}: {total_ventas}\nValor total de ventas en el mes {mes}: {total_valor}\n"
        areasecond.insert(END, resumen)
    else:
        areasecond.insert(END, "\nMes inválido")

def buscarProducto():
    mes = int(entradaNum.get().strip())
    nombre_buscar = entradaPosCol.get().strip().upper()
    tipo_buscar = entradaPosFil.get().strip().upper()

    if 1 <= mes and mes <= 12:
        x = mes - 1
        areasecond.delete("1.0", END)
        encontrado = 0

        for l in range(cont[x]):
            if (nombre_buscar == nombre[x][l]) or (tipo_buscar == tipo[x][l]):
                producto_info = f"Producto: {nombre[x][l]}, Tipo: {tipo[x][l]} \nCantidad: {cantidad[x][l]}, Valor Unitario: {valor[x][l]}\n"
                areasecond.insert(END, producto_info)
                encontrado += 1

        if encontrado == 0:
            areasecond.insert(END, "Producto no encontrado en el mes especificado.\n")

    else:
        areasecond.insert(END, "\nMes inválido")


# ---------------- INTERFAZ GUI -----------------
matriz = Tk()
matriz.geometry("700x600")
matriz.title("INVENTARIO LOCAL")

# Crear notebook (pestañas)
notebook = ttk.Notebook(matriz)
notebook.pack(expand=True, fill="both")

# Crear las pestañas
ingreso = Frame(notebook)
operaciones = Frame(notebook)

# Agregar las pestañas al notebook
notebook.add(ingreso, text="Ingresar Datos")
notebook.add(operaciones, text="Operaciones")

# Contenido primera pestaña
nNom = Label(ingreso, text = "Nombre Producto: ").grid(row = 0, column = 0)
nTip = Label(ingreso, text = "Tipo de Prodcuto: ").grid(row = 1, column = 0 )
nPrecio = Label(ingreso, text = "Valor del Producto: ").grid(row = 2, column = 0)
nCant = Label(ingreso, text = "Cantidad vendida: ").grid(row = 3, column = 0)
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

# Centrar primera pestaña
ingreso.grid_columnconfigure(0, weight=1)
ingreso.grid_columnconfigure(2, weight=1)
ingreso.grid_columnconfigure(1, weight=0)

# Punto de impresion
areaMatriz = Text(ingreso, height=25, width=30)
areaMatriz.grid(row=6, column=0, columnspan=3)
areasecond = Text(operaciones, height=30, width=60)
areasecond.grid(row=5, column=0, columnspan=3)
areasecond.insert(END, "Para Buscar!:\nnombre + numero del mes + buscar.\ncategoria + numero del mes + buscar.\nmes + reporte total del mes.\n--->Recuerda cumplir con los parametros establecidos<---\n")

# Texto en la segunda pestaña
manejo = Label(operaciones, text = "SECCION INVENTARIO!!").grid(row = 0, column = 1)
CambioColum = Label(operaciones, text = "Buscar Producto por nombre: ").grid(row = 1, column = 0)
cambioFila = Label(operaciones, text = "Buscar Producto por Categoría: ").grid(row = 2, column = 0)
numero = Label(operaciones, text = "Número Del Mes: ").grid(row = 3, column = 0)

# Entradas segunda pestaña
entradaPosCol = Entry(operaciones, width = 20)
entradaPosCol.grid(row = 1, column = 1)
entradaPosFil = Entry(operaciones, width = 20)
entradaPosFil.grid(row = 2, column = 1)
entradaNum = Entry(operaciones, width = 20)
entradaNum.grid(row = 3, column = 1)

# Centrar segunda pestaña
operaciones.grid_columnconfigure(0, weight=1)
operaciones.grid_columnconfigure(2, weight=1)
operaciones.grid_columnconfigure(1, weight=0)

# Botones
botonImprimir = Button(ingreso, text = "Ingresar Venta :D", command = ingresarVenta)
botonImprimir.grid(row=5, column=1)
botonIngresar = Button(operaciones, text = "Reporte Total del Mes", command = reporteTotalMes)
botonIngresar.grid(row=4, column = 0)
botonImp = Button(operaciones, text = "    Buscar    ", command = buscarProducto)
botonImp.grid(row=4, column = 1)

matriz.mainloop()
