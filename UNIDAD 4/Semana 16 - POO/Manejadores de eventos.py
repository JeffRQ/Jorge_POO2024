import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Tareas")
        self.root.geometry("400x400")

        # Lista para almacenar las tareas
        self.tasks = []
        # Conjunto para almacenar las tareas completadas
        self.completed_tasks = set()

        # Entrada para ingresar nuevas tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.pack(pady=10)
        # Asigna la tecla "Enter" para añadir una tarea al presionar
        self.task_entry.bind("<Return>", self.add_task)

        # Botón para añadir una nueva tarea
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Botón para completar la tarea seleccionada
        self.complete_button = tk.Button(root, text="Completar Tarea", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Botón para eliminar la tarea seleccionada
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Listbox para mostrar la lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Atajos de teclado
        self.root.bind("<+>", lambda event: self.complete_task())  # Completar tarea con la tecla "+"
        self.root.bind("<Delete>", lambda event: self.delete_task())  # Eliminar tarea con la tecla "Delete"
        self.root.bind("<Escape>", lambda event: self.root.quit())  # Cerrar aplicación con la tecla "Escape"

    # Función para añadir una nueva tarea
    def add_task(self, event=None):
        task = self.task_entry.get()  # Obtener el texto de la entrada
        if task:
            self.tasks.append(task)  # Añadir la tarea a la lista
            self.update_task_listbox()  # Actualizar la lista visual
            self.task_entry.delete(0, tk.END)  # Limpiar la entrada de texto
        else:
            # Mostrar advertencia si no se ha ingresado nada
            messagebox.showwarning("Entrada vacía", "Por favor, ingrese una tarea.")

    # Función para marcar una tarea como completada
    def complete_task(self, event=None):
        selected_task_index = self.task_listbox.curselection()  # Obtener el índice de la tarea seleccionada
        if selected_task_index:
            task = self.task_listbox.get(selected_task_index)  # Obtener el texto de la tarea seleccionada
            if task not in self.completed_tasks:
                self.completed_tasks.add(task)  # Añadir la tarea al conjunto de tareas completadas
                self.update_task_listbox()  # Actualizar la lista visual
            else:
                # Mostrar un mensaje si la tarea ya estaba completada
                messagebox.showinfo("Tarea completada", "Esta tarea ya está completada.")
        else:
            # Mostrar advertencia si no se ha seleccionado ninguna tarea
            messagebox.showwarning("No seleccionada", "Por favor, seleccione una tarea para completar.")

    # Función para eliminar una tarea seleccionada
    def delete_task(self, event=None):
        selected_task_index = self.task_listbox.curselection()  # Obtener el índice de la tarea seleccionada
        if selected_task_index:
            index = selected_task_index[0]  # Obtener el primer índice seleccionado
            task = self.task_listbox.get(index)  # Obtener la tarea desde el índice
            # Remover la tarea de la lista de tareas
            if task in self.tasks:
                self.tasks.remove(task)
            # Remover la tarea de la lista de tareas completadas si es necesario
            if task in self.completed_tasks:
                self.completed_tasks.remove(task)
            self.update_task_listbox()  # Actualizar la lista visual
        else:
            # Mostrar advertencia si no se ha seleccionado ninguna tarea
            messagebox.showwarning("No seleccionada", "Por favor, seleccione una tarea para eliminar.")

    # Función para actualizar la lista visual de tareas en el Listbox
    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)  # Limpiar el Listbox
        for task in self.tasks:
            if task in self.completed_tasks:
                # Mostrar la tarea completada con el texto " (Completada)"
                self.task_listbox.insert(tk.END, f"{task} (Completada)")
            else:
                # Mostrar la tarea sin modificar
                self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()  # Crear la ventana principal de Tkinter
    app = TaskManagerApp(root)  # Inicializar la aplicación
    root.mainloop()  # Ejecutar el bucle principal de la ventana
