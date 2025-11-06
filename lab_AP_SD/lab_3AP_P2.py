import tkinter as tk

def primo(n):
    if n <= 1:
        return False
    con = 2
    while con < n and n % con != 0:
        con += 1
    return con == n

def verificar():
    n = int(entrada.get())
    if primo(n):
        etiqueta_resultado.config(text="El número es primo")
    else:
        etiqueta_resultado.config(text="El número no es primo")

ventana = tk.Tk()
ventana.title("Par o Impar")
ventana.geometry("400x200")

etiqueta = tk.Label(ventana, text="Ingresa un numero entero")
etiqueta.grid(column=0, row=0)

entrada = tk.Entry(ventana, width=25)
entrada.grid(column=0,row=1)

boton = tk.Button(ventana, text="PRIMO", command=verificar)
boton.grid(column=1,row=1)

etiqueta_resultado = tk.Label(ventana, text="El número es: ")
etiqueta_resultado.grid(column=0,row=2)

ventana.mainloop()

