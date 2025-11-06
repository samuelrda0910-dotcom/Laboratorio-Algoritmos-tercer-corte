import tkinter as tk
from tkinter import messagebox

def calcular_imc():
    peso = float(entrada_peso.get())
    estatura = float(entrada_talla.get())

    if peso < 0:
        messagebox.showerror("Error", "el peso no puede ser negativo")
        return
    if estatura < 0:
        messagebox.showerror("Error", "la estatura no puede ser negativa")
        return
    
    imc = peso / estatura ** 2

    if imc >= 30:
        etiqueta_resultado.config(text=f"El IMC es: {imc:.4f}, ¡Urgente! Tienes obesidad")
    elif 25 <= imc <= 39:
        etiqueta_resultado.config(text=f"El IMC es: {imc:.4f}, ¡Cuidado! Tienes sobrepeso")
    elif 19 <= imc <= 24:
        etiqueta_resultado.config(text=f"El IMC es: {imc:.4f}, ¡Excelente! Tienes el peso ideal")
    elif imc < 18:
        etiqueta_resultado.config(text=f"El IMC es: {imc:.4f}, ¡Urgente! Estás baja de peso")

ventana = tk.Tk()
ventana.title("Indice de Masa Corporal")
ventana.geometry("600x200")

etiqueta_peso = tk.Label(ventana, text="Ingrese su peso: ", font=("Arial",15,"bold"))
etiqueta_peso.grid(column=0,row=0)
entrada_peso = tk.Entry(ventana, width=30)
entrada_peso.grid(column=1,row=0)

etiqueta_talla = tk.Label(ventana, text="Ingrese su estatura: ", font=("Arial",15,"bold"))
etiqueta_talla.grid(column=0,row=1)
entrada_talla = tk.Entry(ventana, width=30)
entrada_talla.grid(column=1,row=1)

boton = tk.Button(ventana, text="CALCULAR IMC", command=calcular_imc)
boton.config(font=("Arial",15,"bold"))
boton.grid(column=0,row=2)

etiqueta_resultado = tk.Label(ventana, text="Tu IMC es: ", font=("Arial",15,"bold"))
etiqueta_resultado.grid(column=0,row=3)

ventana.mainloop()