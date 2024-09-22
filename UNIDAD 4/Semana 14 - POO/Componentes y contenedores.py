import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from tkcalendar import DateEntry

# Crear la ventana principal
root = tk.Tk()
root.title("AGENDA PERSONAL")  # Título de la ventana
root.geometry('800x500')  # Tamaño de la ventana


# Función para agregar un evento a la lista
def agregar_evento():
    fecha = date_picker.get()  # Obtener la fecha seleccionada
    hora = hora_entry.get()  # Obtener la hora ingresada
    descripcion = descripcion_entry.get()  # Obtener la descripción ingresada

    # Verificar que los campos no estén vacíos
    if descripcion.strip() and hora.strip():  # Validar que haya descripción y hora
        # Insertar los valores en el Treeview como una nueva fila
        tree.insert("", "end", values=(fecha, hora, descripcion))
        descripcion_entry.delete(0, tk.END)  # Limpiar el campo de descripción después de agregar el evento
        hora_entry.delete(0, tk.END)  # Limpiar el campo de hora después de agregar el evento
    else:
        messagebox.showwarning("Campos vacíos", "Por favor, ingrese la hora y la descripción.")


# Función para eliminar el evento seleccionado de la lista
def eliminar_evento():
    selected_item = tree.selection()  # Obtener el ítem seleccionado
    if selected_item:  # Verificar si hay un ítem seleccionado
        # Mostrar un cuadro de confirmación
        confirmacion = messagebox.askyesno("¿Está seguro de eliminar?", "Eliminar")

        if confirmacion:  # Si se confirma, eliminar el ítem
            tree.delete(selected_item)
    else:
        # Mostrar una advertencia si no hay un ítem seleccionado
        messagebox.showwarning("Seleccione", "Seleccione un ítem")


# Función para salir de la aplicación
def salir():
    root.quit()  # Finalizar el bucle principal y cerrar la aplicación


# Crear el frame principal donde se colocarán los componentes
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)  # Ubicar el frame en la ventana

# Etiqueta de título
titulo = ttk.Label(frame, text="AGENDA PERSONAL")
titulo.grid(row=0, column=0, columnspan=2, sticky=tk.NSEW)  # Colocar el título en el frame

# Selector de fecha (DateEntry)
date_picker = DateEntry(frame, date_pattern="y-mm-dd", width=12)  # Widget para seleccionar fechas
date_picker.set_date(date.today())  # Establecer la fecha actual como valor predeterminado
date_picker.grid(row=1, column=0, pady=5)  # Ubicar el selector de fecha en el frame

# Etiqueta y campo de entrada para la hora
hora_label = ttk.Label(frame, text="Ingrese la hora (HH:MM):")  # Etiqueta para la hora
hora_label.grid(row=2, column=0, pady=5)  # Ubicar la etiqueta de la hora en el frame

hora_entry = ttk.Entry(frame)  # Campo de entrada para la hora
hora_entry.grid(row=2, column=1, pady=5)  # Ubicar el campo de entrada de la hora en el frame

# Etiqueta y campo de entrada para la descripción
descripcion_label = ttk.Label(frame, text="Descripción:")  # Etiqueta para la descripción
descripcion_label.grid(row=3, column=0, pady=5)  # Ubicar la etiqueta de descripción

descripcion_entry = ttk.Entry(frame)  # Campo de entrada para la descripción
descripcion_entry.grid(row=3, column=1, pady=5)  # Ubicar el campo de entrada de la descripción

# Botón para agregar el evento
agregar_boton = ttk.Button(frame, text="Agregar Evento", command=agregar_evento)
agregar_boton.grid(row=4, column=0, pady=5)  # Ubicar el botón de "Agregar Evento"

# Tabla (Treeview) para mostrar los eventos en forma de lista
tree = ttk.Treeview(frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.grid(row=5, column=0, columnspan=2, sticky="nsew")  # Ubicar la tabla en el frame

# Definir los encabezados de las columnas
tree.heading("Fecha", text="Fecha")  # Encabezado para la columna "Fecha"
tree.heading("Hora", text="Hora")  # Encabezado para la columna "Hora"
tree.heading("Descripción", text="Descripción")  # Encabezado para la columna "Descripción"

# Botón para eliminar el evento seleccionado
eliminar_boton = ttk.Button(frame, text="Eliminar Evento Seleccionado", command=eliminar_evento)
eliminar_boton.grid(row=6, column=0, pady=5)  # Ubicar el botón de "Eliminar Evento Seleccionado"

# Botón para salir de la aplicación
salir_boton = ttk.Button(frame, text="Salir", command=salir)
salir_boton.grid(row=6, column=1, pady=5)  # Ubicar el botón de "Salir"

# Iniciar el bucle principal de la aplicación
root.mainloop()  # Esto mantiene la ventana abierta y en funcionamiento
