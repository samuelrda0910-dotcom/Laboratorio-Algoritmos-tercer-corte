import tkinter as tk

def precio_cuaderno():
    paginas = int(entrada.get())

    if 101 <= paginas <= 250:
        precio = 16000
    elif 81 <= paginas <= 100:
        precio = 11000
    elif 51 <= paginas <= 80:
        precio = 8000
    elif 1 <= paginas <= 50:
        precio = 4500
    else:
        precio = "Numero fuera de rango (1-250)"
    
    etiqueta_resultado.config(text=f"Precio del cuaderno: {precio} pesos")

ventana = tk.Tk()
ventana.title("Costo de cuaderno")
ventana.geometry("400x200")

etiqueta = tk.Label(ventana, text="Ingrese el numero de hojas del cuaderno, (1-250)")
etiqueta.grid(column=0,row=0)

entrada = tk.Entry(ventana, width=25)
entrada.grid(column=0,row=1)

boton_precio = tk.Button(ventana, text="Precio", command=precio_cuaderno)
boton_precio.grid(column=1,row=1)

etiqueta_resultado = tk.Label(ventana, text="El precio del cuaderno es: ", font=("Arial",12,"bold"))
etiqueta_resultado.grid(column=0,row=2)


ventana.mainloop()