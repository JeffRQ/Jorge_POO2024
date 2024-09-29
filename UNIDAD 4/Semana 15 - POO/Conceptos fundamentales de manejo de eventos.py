import tkinter as tk
from tkinter import messagebox

class ListaTareasApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lista de Tareas")

        # Campo de entrada para nuevas tareas
        self.entrada_tarea = tk.Entry(self.root, width=40)
        self.entrada_tarea.grid(row=0, column=0, padx=10, pady=10)

        # Botón para añadir tarea
        self.boton_añadir = tk.Button(self.root, text="Añadir Tarea", command=self.añadir_tarea)
        self.boton_añadir.grid(row=0, column=1, padx=10, pady=10)

        # Lista de tareas (Listbox)
        self.lista_tareas = tk.Listbox(self.root, width=50, height=10)
        self.lista_tareas.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        # Botón para marcar tarea como completada
        self.boton_completada = tk.Button(self.root, text="Marcar como Completada", command=self.marcar_completada)
        self.boton_completada.grid(row=2, column=0, padx=10, pady=10)

        # Botón para eliminar tarea
        self.boton_eliminar = tk.Button(self.root, text="Eliminar Tarea", command=self.eliminar_tarea)
        self.boton_eliminar.grid(row=2, column=1, padx=10, pady=10)

        # Vincular la tecla Enter para añadir una tarea
        self.root.bind('<Return>', self.añadir_tarea)

    # Función para añadir una nueva tarea a la lista
    def añadir_tarea(self, event=None):
        tarea = self.entrada_tarea.get()
        if tarea != "":
            self.lista_tareas.insert(tk.END, tarea)
            self.entrada_tarea.delete(0, tk.END)  # Limpiar el campo de entrada
        else:
            messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

    # Función para marcar una tarea como completada
    def marcar_completada(self):
        try:
            index = self.lista_tareas.curselection()[0]  # Obtener el índice de la tarea seleccionada
            tarea = self.lista_tareas.get(index)
            self.lista_tareas.delete(index)
            self.lista_tareas.insert(tk.END, tarea + " (Completada)")  # Marcar la tarea como completada
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    # Función para eliminar una tarea de la lista
    def eliminar_tarea(self):
        try:
            index = self.lista_tareas.curselection()[0]  # Obtener el índice de la tarea seleccionada
            self.lista_tareas.delete(index)
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

# Crear la ventana principal e iniciar la aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = ListaTareasApp(root)
    root.mainloop()
