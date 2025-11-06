import tkinter as tk
from tkinter import messagebox

def calcular():
    a = float(entrada_a.get())
    b = float(entrada_b.get())
    c = float(entrada_c.get())
    
    if b == 0:
        messagebox.showerror("Error, b no puede ser 0")
        return
    if c == 0:
        messagebox.showerror("Error, c no puede ser 0")
        return
    if a == b:
        messagebox.showerror("Error, a y b deben ser diferentes")
        return
    numerador = -b + 5*a + 2*c
    denominador = 2*b*c - c

    if denominador == 0:
        messagebox.showerror("Error, el denominador no puede ser igual a 0")
        return
    
    ec = numerador / denominador

    etiqueta_resultado.config(text=f"Ec = {ec:.4f}")

ventana = tk.Tk()
ventana.title("Calculador de Ecuación = (-b+5a+2c)/(2bc-c)")
ventana.geometry("600x400")

etiqueta = tk.Label(ventana, text="(-b+5a+2c)/(2bc-c)")
etiqueta.config(font=("Arial", 20, "bold"))
etiqueta.grid(column=0,row=0)

etiqueta_b = tk.Label(ventana, text="Valor de b, (no puede ser 0): ", font=("Arial",15))
etiqueta_b.grid(column=0,row=1)
entrada_b = tk.Entry(ventana,width=30)
entrada_b.grid(column=0,row=2)

etiqueta_a = tk.Label(ventana, text="Valor de a, (diferente de b): ", font=("Arial",15))
etiqueta_a.grid(column=0,row=3)
entrada_a = tk.Entry(ventana, width=30)
entrada_a.grid(column=0,row=4)

etiqueta_c = tk.Label(ventana,text="Valor de c, (no puede ser 0): ", font=("Arial",15))
etiqueta_c.grid(column=0,row=5)
entrada_c = tk.Entry(ventana, width=30)
entrada_c.grid(column=0,row=6)

boton = tk.Button(ventana, text="CALCULAR", command=calcular)
boton.config(font=("Arial",15,"bold"))
boton.grid(column=1,row=1)

etiqueta_resultado = tk.Label(ventana, text="Resultado Ec = ", font=("Arial",15,"bold"))
etiqueta_resultado.grid(column=1,row=4)

ventana.mainloop()