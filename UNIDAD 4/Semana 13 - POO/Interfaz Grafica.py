import tkinter as tk
from tkinter import messagebox

# Función para agregar información a la lista
def agregar():
    """
    Obtiene el texto del campo de entrada y lo agrega a la lista si no está vacío.
    Limpia el campo de texto después de agregar el dato. Muestra una advertencia
    si el campo de texto está vacío.
    """
    dato = entrada.get()  # Obtiene el texto ingresado en el campo de texto
    if dato:  # Verifica si el campo de texto no está vacío
        lista_datos.insert(tk.END, dato)  # Agrega el dato a la lista al final
        entrada.delete(0, tk.END)  # Limpia el campo de texto
    else:
        # Muestra una advertencia si el campo está vacío
        messagebox.showwarning("Advertencia", "Por favor, ingresa algún dato.")

# Función para limpiar la información
def limpiar():
    """
    Elimina el elemento seleccionado de la lista si hay alguno seleccionado.
    Si no hay ningún elemento seleccionado, limpia el campo de texto.
    """
    if lista_datos.curselection():  # Verifica si hay un elemento seleccionado en la lista
        # Elimina el elemento seleccionado de la lista
        lista_datos.delete(lista_datos.curselection())
    else:
        # Limpia el campo de texto si no hay ningún elemento seleccionado
        entrada.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()  # Inicializa la ventana principal
ventana.title("Aplicación de Gestión de Datos")  # Establece el título de la ventana

# Crear y agregar los componentes a la ventana
etiqueta = tk.Label(ventana, text="Ingrese un dato y haga clic en 'Agregar':")
# Crea una etiqueta con instrucciones para el usuario
etiqueta.pack(pady=10)  # Agrega la etiqueta a la ventana con un espacio vertical de 10 píxeles

entrada = tk.Entry(ventana, width=50)
# Crea un campo de texto para la entrada de datos
entrada.pack(pady=5)  # Agrega el campo de texto a la ventana con un espacio vertical de 5 píxeles

boton_agregar = tk.Button(ventana, text="Agregar", command=agregar)
# Crea un botón para agregar datos a la lista
boton_agregar.pack(pady=5)  # Agrega el botón a la ventana con un espacio vertical de 5 píxeles

boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar)
# Crea un botón para limpiar la lista o el campo de texto
boton_limpiar.pack(pady=5)  # Agrega el botón a la ventana con un espacio vertical de 5 píxeles

lista_datos = tk.Listbox(ventana, width=50, height=10)
# Crea una lista para mostrar los datos agregados
lista_datos.pack(pady=10)  # Agrega la lista a la ventana con un espacio vertical de 10 píxeles

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()  # Mantiene la ventana abierta y responde a eventos del usuario
