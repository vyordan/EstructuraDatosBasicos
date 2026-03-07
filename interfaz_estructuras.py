# interfaz_estructuras.py
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import estructuras  # Este es el módulo compilado con pybind11

class AplicacionEstructuras:
    def __init__(self, root):
        self.root = root
        self.root.title("Estructuras de Datos - Pila, Cola, Listas")
        self.root.geometry("900x700")
        
        # Crear las estructuras de datos
        self.pila = estructuras.Pila()
        self.cola = estructuras.Cola()
        self.lista_simple = estructuras.ListaSimple()
        self.lista_doble = estructuras.ListaDoble()
        
        self.estructura_actual = None
        self.nombre_estructura = ""
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        titulo = ttk.Label(main_frame, text="ESTRUCTURAS DE DATOS", font=("Arial", 16, "bold"))
        titulo.grid(row=0, column=0, columnspan=3, pady=10)
        
        # Frame para selección de estructura
        frame_seleccion = ttk.LabelFrame(main_frame, text="Seleccionar Estructura", padding="10")
        frame_seleccion.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        ttk.Button(frame_seleccion, text="Pila", 
                  command=lambda: self.seleccionar_estructura("pila")).grid(row=0, column=0, padx=5)
        ttk.Button(frame_seleccion, text="Cola", 
                  command=lambda: self.seleccionar_estructura("cola")).grid(row=0, column=1, padx=5)
        ttk.Button(frame_seleccion, text="Lista Simple", 
                  command=lambda: self.seleccionar_estructura("lista_simple")).grid(row=0, column=2, padx=5)
        ttk.Button(frame_seleccion, text="Lista Doble", 
                  command=lambda: self.seleccionar_estructura("lista_doble")).grid(row=0, column=3, padx=5)
        
        self.label_estructura = ttk.Label(frame_seleccion, text="Estructura seleccionada: Ninguna", font=("Arial", 10, "bold"))
        self.label_estructura.grid(row=1, column=0, columnspan=4, pady=5)
        
        # Frame para operaciones
        frame_operaciones = ttk.LabelFrame(main_frame, text="Operaciones", padding="10")
        frame_operaciones.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=5)
        
        # Entrada de valor
        ttk.Label(frame_operaciones, text="Valor:").grid(row=0, column=0, padx=5)
        self.entry_valor = ttk.Entry(frame_operaciones, width=15)
        self.entry_valor.grid(row=0, column=1, padx=5)
        
        # Botones de operaciones básicas
        self.btn_insertar = ttk.Button(frame_operaciones, text="Insertar", 
                                       command=self.insertar, state=tk.DISABLED)
        self.btn_insertar.grid(row=1, column=0, padx=5, pady=5)
        
        self.btn_eliminar = ttk.Button(frame_operaciones, text="Eliminar", 
                                       command=self.eliminar, state=tk.DISABLED)
        self.btn_eliminar.grid(row=1, column=1, padx=5, pady=5)
        
        self.btn_buscar = ttk.Button(frame_operaciones, text="Buscar", 
                                     command=self.buscar, state=tk.DISABLED)
        self.btn_buscar.grid(row=1, column=2, padx=5, pady=5)
        
        self.btn_mostrar = ttk.Button(frame_operaciones, text="Mostrar Todo", 
                                      command=self.mostrar, state=tk.DISABLED)
        self.btn_mostrar.grid(row=2, column=0, padx=5, pady=5)
        
        self.btn_vaciar = ttk.Button(frame_operaciones, text="Vaciar", 
                                     command=self.vaciar, state=tk.DISABLED)
        self.btn_vaciar.grid(row=2, column=1, padx=5, pady=5)
        
        # Posición para listas
        ttk.Label(frame_operaciones, text="Posición:").grid(row=0, column=2, padx=5)
        self.entry_posicion = ttk.Entry(frame_operaciones, width=10)
        self.entry_posicion.grid(row=0, column=3, padx=5)
        
        self.btn_insertar_pos = ttk.Button(frame_operaciones, text="Insertar en Posición", 
                                          command=self.insertar_posicion, state=tk.DISABLED)
        self.btn_insertar_pos.grid(row=1, column=3, padx=5, pady=5)
        
        self.btn_obtener_pos = ttk.Button(frame_operaciones, text="Obtener de Posición", 
                                         command=self.obtener_posicion, state=tk.DISABLED)
        self.btn_obtener_pos.grid(row=2, column=3, padx=5, pady=5)
        
        # Frame para mostrar resultados
        frame_resultado = ttk.LabelFrame(main_frame, text="Resultados", padding="10")
        frame_resultado.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=5)
        
        self.text_resultado = scrolledtext.ScrolledText(frame_resultado, width=80, height=15)
        self.text_resultado.grid(row=0, column=0, columnspan=2, padx=5, pady=5)
        
        # Botón de limpiar
        ttk.Button(frame_resultado, text="Limpiar Resultados", 
                  command=self.limpiar_resultados).grid(row=1, column=0, pady=5)
        
        # Configurar grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        main_frame.rowconfigure(3, weight=1)
        frame_resultado.columnconfigure(0, weight=1)
        frame_resultado.rowconfigure(0, weight=1)
        
    def seleccionar_estructura(self, tipo):
        if tipo == "pila":
            self.estructura_actual = self.pila
            self.nombre_estructura = "Pila"
            self.btn_insertar.config(text="Apilar")
            self.btn_eliminar.config(text="Desapilar")
            self.btn_buscar.config(state=tk.NORMAL)
            self.btn_insertar_pos.config(state=tk.DISABLED)
            self.btn_obtener_pos.config(state=tk.DISABLED)
        elif tipo == "cola":
            self.estructura_actual = self.cola
            self.nombre_estructura = "Cola"
            self.btn_insertar.config(text="Encolar")
            self.btn_eliminar.config(text="Desencolar")
            self.btn_buscar.config(state=tk.NORMAL)
            self.btn_insertar_pos.config(state=tk.DISABLED)
            self.btn_obtener_pos.config(state=tk.DISABLED)
        elif tipo == "lista_simple":
            self.estructura_actual = self.lista_simple
            self.nombre_estructura = "Lista Simple"
            self.btn_insertar.config(text="Insertar Final")
            self.btn_eliminar.config(text="Eliminar")
            self.btn_buscar.config(state=tk.NORMAL)
            self.btn_insertar_pos.config(state=tk.NORMAL)
            self.btn_obtener_pos.config(state=tk.NORMAL)
        elif tipo == "lista_doble":
            self.estructura_actual = self.lista_doble
            self.nombre_estructura = "Lista Doble"
            self.btn_insertar.config(text="Insertar Final")
            self.btn_eliminar.config(text="Eliminar")
            self.btn_buscar.config(state=tk.NORMAL)
            self.btn_insertar_pos.config(state=tk.NORMAL)
            self.btn_obtener_pos.config(state=tk.NORMAL)
        
        self.label_estructura.config(text=f"Estructura seleccionada: {self.nombre_estructura}")
        self.btn_insertar.config(state=tk.NORMAL)
        self.btn_eliminar.config(state=tk.NORMAL)
        self.btn_mostrar.config(state=tk.NORMAL)
        self.btn_vaciar.config(state=tk.NORMAL)
        self.mostrar()
        
    def insertar(self):
        try:
            valor = int(self.entry_valor.get())
            if self.nombre_estructura == "Pila":
                self.estructura_actual.apilar(valor)
                self.mostrar_mensaje(f"Apilado: {valor}")
            elif self.nombre_estructura == "Cola":
                self.estructura_actual.encolar(valor)
                self.mostrar_mensaje(f"Encolado: {valor}")
            else:  # Listas
                self.estructura_actual.insertar_final(valor)
                self.mostrar_mensaje(f"Insertado: {valor} al final")
            
            self.mostrar()
            self.entry_valor.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico válido")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def eliminar(self):
        try:
            if self.nombre_estructura == "Pila":
                if not self.estructura_actual.esta_vacia():
                    valor = self.estructura_actual.desapilar()
                    self.mostrar_mensaje(f"Desapilado: {valor}")
                else:
                    messagebox.showwarning("Advertencia", "La pila está vacía")
            elif self.nombre_estructura == "Cola":
                if not self.estructura_actual.esta_vacia():
                    valor = self.estructura_actual.desencolar()
                    self.mostrar_mensaje(f"Desencolado: {valor}")
                else:
                    messagebox.showwarning("Advertencia", "La cola está vacía")
            else:  # Listas
                valor = int(self.entry_valor.get())
                if self.estructura_actual.eliminar(valor):
                    self.mostrar_mensaje(f"Eliminado: {valor}")
                else:
                    messagebox.showinfo("Info", f"Valor {valor} no encontrado")
            
            self.mostrar()
            self.entry_valor.delete(0, tk.END)
        except ValueError:
            if self.nombre_estructura in ["Lista Simple", "Lista Doble"]:
                messagebox.showerror("Error", "Ingrese un valor numérico para eliminar")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def buscar(self):
        try:
            valor = int(self.entry_valor.get())
            encontrado = self.estructura_actual.buscar(valor)
            if encontrado:
                self.mostrar_mensaje(f"Valor {valor} ENCONTRADO en la {self.nombre_estructura}")
            else:
                self.mostrar_mensaje(f"Valor {valor} NO encontrado en la {self.nombre_estructura}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un valor numérico para buscar")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def insertar_posicion(self):
        if self.nombre_estructura not in ["Lista Simple", "Lista Doble"]:
            return
        
        try:
            valor = int(self.entry_valor.get())
            posicion = int(self.entry_posicion.get())
            self.estructura_actual.insertar_en_posicion(valor, posicion)
            self.mostrar_mensaje(f"Insertado {valor} en posición {posicion}")
            self.mostrar()
            self.entry_valor.delete(0, tk.END)
            self.entry_posicion.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def obtener_posicion(self):
        if self.nombre_estructura not in ["Lista Simple", "Lista Doble"]:
            return
        
        try:
            posicion = int(self.entry_posicion.get())
            valor = self.estructura_actual.obtener(posicion)
            self.mostrar_mensaje(f"En posición {posicion}: {valor}")
            self.entry_posicion.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Ingrese una posición numérica válida")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def mostrar(self):
        try:
            contenido = ""
            if self.nombre_estructura == "Pila":
                contenido = self.estructura_actual.mostrar()
            elif self.nombre_estructura == "Cola":
                contenido = self.estructura_actual.mostrar()
            elif self.nombre_estructura == "Lista Simple":
                contenido = self.estructura_actual.mostrar()
            elif self.nombre_estructura == "Lista Doble":
                contenido = self.estructura_actual.mostrar_adelante()
            
            self.text_resultado.delete(1.0, tk.END)
            self.text_resultado.insert(tk.END, f"{self.nombre_estructura}:\n")
            self.text_resultado.insert(tk.END, f"Elementos: {contenido}\n")
            self.text_resultado.insert(tk.END, f"Tamaño: {self.estructura_actual.tamano()}")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            
    def vaciar(self):
        if messagebox.askyesno("Confirmar", f"¿Vaciar la {self.nombre_estructura}?"):
            if self.nombre_estructura == "Pila":
                self.pila = estructuras.Pila()
                self.estructura_actual = self.pila
            elif self.nombre_estructura == "Cola":
                self.cola = estructuras.Cola()
                self.estructura_actual = self.cola
            elif self.nombre_estructura == "Lista Simple":
                self.lista_simple = estructuras.ListaSimple()
                self.estructura_actual = self.lista_simple
            elif self.nombre_estructura == "Lista Doble":
                self.lista_doble = estructuras.ListaDoble()
                self.estructura_actual = self.lista_doble
            
            self.mostrar()
            self.mostrar_mensaje(f"{self.nombre_estructura} vaciada")
            
    def mostrar_mensaje(self, mensaje):
        self.text_resultado.insert(tk.END, f"\n> {mensaje}")
        self.text_resultado.see(tk.END)
        
    def limpiar_resultados(self):
        self.text_resultado.delete(1.0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = AplicacionEstructuras(root)
    root.mainloop()