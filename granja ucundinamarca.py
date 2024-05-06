import tkinter as tk
from tkinter import simpledialog, messagebox

class Produccion:
    def calcular_produccion(self):
        pass

class Cultivo(Produccion):
    def __init__(self, nombre, tipo, area, rendimiento):
        self.nombre = nombre
        self.tipo = tipo
        self.area = area
        self.rendimiento = rendimiento

    def calcular_produccion(self):
        return self.area * self.rendimiento

    def __str__(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}, Área: {self.area} m², Rendimiento: {self.rendimiento} kg/m²"

class Animal(Produccion):
    def __init__(self, especie, raza, edad, peso):
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def calcular_produccion(self):
        # Aquí puedes implementar un cálculo más complejo basado en la especie, raza, etc.
        return self.peso

    def __str__(self):
        return f"Especie: {self.especie}, Raza: {self.raza}, Edad: {self.edad} años, Peso: {self.peso} kg"

class Granja:
    def __init__(self):
        self.cultivos = []
        self.animales = []

    def agregar_cultivo(self, cultivo):
        self.cultivos.append(cultivo)

    def eliminar_cultivo(self, nombre):
        for cultivo in self.cultivos:
            if cultivo.nombre == nombre:
                self.cultivos.remove(cultivo)
                return
        messagebox.showerror("Error", f"No se encontró un cultivo con el nombre '{nombre}'")

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def eliminar_animal(self, especie):
        for animal in self.animales:
            if animal.especie == especie:
                self.animales.remove(animal)
                return
        messagebox.showerror("Error", f"No se encontró un animal de la especie '{especie}'")

    def calcular_produccion_total(self):
        produccion_cultivos = sum(cultivo.calcular_produccion() for cultivo in self.cultivos)
        produccion_animales = sum(animal.calcular_produccion() for animal in self.animales)
        return produccion_cultivos + produccion_animales

    def obtener_informacion(self):
        info_cultivos = "\n".join(str(cultivo) for cultivo in self.cultivos)
        info_animales = "\n".join(str(animal) for animal in self.animales)
        return f"--- Cultivos ---\n{info_cultivos}\n\n--- Animales ---\n{info_animales}"

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Sistema de Gestión Granja Ucundinamarca")

        self.granja = Granja()

        # Crear widgets
        self.lbl_title = tk.Label(master, text="Gestión de Granja")
        self.lbl_title.grid(row=0, column=0, columnspan=3)

        self.btn_agregar_cultivo = tk.Button(master, text="Agregar Cultivo", command=self.agregar_cultivo)
        self.btn_agregar_cultivo.grid(row=1, column=0)

        self.btn_eliminar_cultivo = tk.Button(master, text="Eliminar Cultivo", command=self.eliminar_cultivo)
        self.btn_eliminar_cultivo.grid(row=1, column=1)

        self.btn_agregar_animal = tk.Button(master, text="Agregar Animal", command=self.agregar_animal)
        self.btn_agregar_animal.grid(row=1, column=2)

        self.btn_eliminar_animal = tk.Button(master, text="Eliminar Animal", command=self.eliminar_animal)
        self.btn_eliminar_animal.grid(row=1, column=3)

        self.btn_info_granja = tk.Button(master, text="Información de Granja", command=self.mostrar_info_granja)
        self.btn_info_granja.grid(row=2, column=0, columnspan=4)

        self.lbl_produccion_total = tk.Label(master, text="Producción Total:")
        self.lbl_produccion_total.grid(row=3, column=0, columnspan=4)

        self.btn_calcular_produccion = tk.Button(master, text="Calcular Producción", command=self.calcular_produccion)
        self.btn_calcular_produccion.grid(row=4, column=0, columnspan=4)

    def agregar_cultivo(self):
        nombre = simpledialog.askstring("Agregar Cultivo", "Nombre del cultivo:")
        tipo = simpledialog.askstring("Agregar Cultivo", "Tipo de cultivo:")
        area = simpledialog.askfloat("Agregar Cultivo", "Área de cultivo (en metros cuadrados):")
        rendimiento = simpledialog.askfloat("Agregar Cultivo", "Rendimiento (en kg/m²):")
        cultivo = Cultivo(nombre, tipo, area, rendimiento)
        self.granja.agregar_cultivo(cultivo)

    def eliminar_cultivo(self):
        nombre = simpledialog.askstring("Eliminar Cultivo", "Nombre del cultivo a eliminar:")
        self.granja.eliminar_cultivo(nombre)

    def agregar_animal(self):
        especie = simpledialog.askstring("Agregar Animal", "Especie del animal:")
        raza = simpledialog.askstring("Agregar Animal", "Raza del animal:")
        edad = simpledialog.askinteger("Agregar Animal", "Edad del animal:")
        peso = simpledialog.askfloat("Agregar Animal", "Peso del animal (en kg):")
        animal = Animal(especie, raza, edad, peso)
        self.granja.agregar_animal(animal)

    def eliminar_animal(self):
        especie = simpledialog.askstring("Eliminar Animal", "Especie del animal a eliminar:")
        self.granja.eliminar_animal(especie)

    def mostrar_info_granja(self):
        info_granja = self.granja.obtener_informacion()
        messagebox.showinfo("Información de Granja", info_granja)

    def calcular_produccion(self):
        produccion_total = self.granja.calcular_produccion_total()
        self.lbl_produccion_total.config(text=f"Producción Total: {produccion_total}")

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    app = GUI(root)
    root.mainloop()
