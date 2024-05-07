import tkinter as tk
from tkinter import messagebox
import sqlite3

class RegistroAlumnosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Alumnos")
        self.root.configure(bg='lightblue')

        # Conexión a la base de datos
        self.conn = sqlite3.connect('alumnos.db')
        self.c = self.conn.cursor()

        # Crear tabla si no existe
        self.c.execute('''CREATE TABLE IF NOT EXISTS alumnos (
                            id INTEGER PRIMARY KEY,
                            nombre TEXT NOT NULL,
                            edad INTEGER,
                            curso TEXT
                        )''')
        self.conn.commit()

        # Etiquetas y cuadros de entrada
        tk.Label(root, text="Nombre:", bg='lightblue').grid(row=0, column=0)
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.grid(row=0, column=1)

        tk.Label(root, text="Edad:", bg='lightblue').grid(row=1, column=0)
        self.edad_entry = tk.Entry(root)
        self.edad_entry.grid(row=1, column=1)

        tk.Label(root, text="Curso:", bg='lightblue').grid(row=2, column=0)
        self.curso_entry = tk.Entry(root)
        self.curso_entry.grid(row=2, column=1)

        # Botones
        self.guardar_button = tk.Button(root, text="Guardar", bg='green', fg='white', command=self.guardar_alumno)
        self.guardar_button.grid(row=3, column=0, columnspan=2, pady=10)

        self.mostrar_button = tk.Button(root, text="Mostrar", bg='blue', fg='white', command=self.mostrar_alumnos)
        self.mostrar_button.grid(row=4, column=0, columnspan=2)

    def guardar_alumno(self):
        nombre = self.nombre_entry.get()
        edad = self.edad_entry.get()
        curso = self.curso_entry.get()

        if nombre and edad and curso:
            self.c.execute("INSERT INTO alumnos (nombre, edad, curso) VALUES (?, ?, ?)", (nombre, edad, curso))
            self.conn.commit()
            messagebox.showinfo("Éxito", "Alumno guardado correctamente.")
        else:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")

    def mostrar_alumnos(self):
        self.c.execute("SELECT * FROM alumnos")
        alumnos = self.c.fetchall()
        if alumnos:
            messagebox.showinfo("Alumnos Registrados", "\n".join([f"{alumno[0]}. {alumno[1]} - Edad: {alumno[2]} - Curso: {alumno[3]}" for alumno in alumnos]))
        else:
            messagebox.showinfo("Alumnos Registrados", "No hay alumnos registrados.")

if __name__ == "__main__":
    root = tk.Tk()
    app = RegistroAlumnosApp(root)
    root.mainloop()