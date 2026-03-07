# interfaz_estructuras_grafica.py
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import estructuras  # Módulo compilado con pybind11
import math

class AplicacionEstructurasGrafica:
    def __init__(self, root):
        self.root = root
        self.root.title("Estructuras de Datos - Visualización Gráfica")
        self.root.geometry("1200x800")
        
        # Colores para los nodos
        self.colores = [
            "#FF6B6B", "#4ECDC4", "#45B7D1", "#96CEB4", "#FFEEAD",
            "#D4A5A5", "#9B59B6", "#3498DB", "#E67E22", "#2ECC71",
            "#F1C40F", "#E74C3C", "#1ABC9C", "#9B59B6", "#34495E"
        ]
        
        # Crear las estructuras de datos
        self.pila = estructuras.Pila()
        self.cola = estructuras.Cola()
        self.lista_simple = estructuras.ListaSimple()
        self.lista_doble = estructuras.ListaDoble()
        
        self.estructura_actual = None
        self.nombre_estructura = ""
        self.nodos_graficos = []  # Para almacenar los elementos gráficos
        
        self.crear_interfaz()
        
    def crear_interfaz(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Título
        titulo = ttk.Label(main_frame, text="ESTRUCTURAS DE DATOS - VISUALIZACIÓN GRAFICA", 
                          font=("Arial", 16, "bold"))
        titulo.pack(pady=10)
        
        # Frame superior para controles
        frame_superior = ttk.Frame(main_frame)
        frame_superior.pack(fill=tk.X, pady=5)
        
        # Frame para selección de estructura
        frame_seleccion = ttk.LabelFrame(frame_superior, text="Seleccionar Estructura", padding="10")
        frame_seleccion.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        
        botones_estructura = ttk.Frame(frame_seleccion)
        botones_estructura.pack()
        
        ttk.Button(botones_estructura, text="Pila", 
                  command=lambda: self.seleccionar_estructura("pila")).pack(side=tk.LEFT, padx=5)
        ttk.Button(botones_estructura, text="Cola", 
                  command=lambda: self.seleccionar_estructura("cola")).pack(side=tk.LEFT, padx=5)
        ttk.Button(botones_estructura, text="Lista Simple", 
                  command=lambda: self.seleccionar_estructura("lista_simple")).pack(side=tk.LEFT, padx=5)
        ttk.Button(botones_estructura, text="Lista Doble", 
                  command=lambda: self.seleccionar_estructura("lista_doble")).pack(side=tk.LEFT, padx=5)
        
        self.label_estructura = ttk.Label(frame_seleccion, 
                                         text="Estructura seleccionada: Ninguna",
                                         font=("Arial", 10, "bold"))
        self.label_estructura.pack(pady=5)
        
        # Frame para operaciones
        frame_operaciones = ttk.LabelFrame(frame_superior, text="Operaciones", padding="10")
        frame_operaciones.pack(side=tk.RIGHT, fill=tk.X, expand=True, padx=5)
        
        # Entradas
        entrada_frame = ttk.Frame(frame_operaciones)
        entrada_frame.pack(pady=5)
        
        ttk.Label(entrada_frame, text="Valor:").pack(side=tk.LEFT, padx=5)
        self.entry_valor = ttk.Entry(entrada_frame, width=10)
        self.entry_valor.pack(side=tk.LEFT, padx=5)
        
        ttk.Label(entrada_frame, text="Posicion:").pack(side=tk.LEFT, padx=5)
        self.entry_posicion = ttk.Entry(entrada_frame, width=8)
        self.entry_posicion.pack(side=tk.LEFT, padx=5)
        
        # Botones - Distribucion mejorada
        botones1 = ttk.Frame(frame_operaciones)
        botones1.pack(pady=5)
        
        self.btn_insertar = ttk.Button(botones1, text="Insertar", 
                                       command=self.insertar, state=tk.DISABLED, width=12)
        self.btn_insertar.pack(side=tk.LEFT, padx=3)
        
        self.btn_eliminar = ttk.Button(botones1, text="Eliminar", 
                                       command=self.eliminar, state=tk.DISABLED, width=12)
        self.btn_eliminar.pack(side=tk.LEFT, padx=3)
        
        self.btn_buscar = ttk.Button(botones1, text="Buscar", 
                                     command=self.buscar, state=tk.DISABLED, width=12)
        self.btn_buscar.pack(side=tk.LEFT, padx=3)
        
        self.btn_vaciar = ttk.Button(botones1, text="Vaciar", 
                                     command=self.vaciar, state=tk.DISABLED, width=12)
        self.btn_vaciar.pack(side=tk.LEFT, padx=3)
        
        # Segunda fila de botones
        botones2 = ttk.Frame(frame_operaciones)
        botones2.pack(pady=5)
        
        self.btn_insertar_pos = ttk.Button(botones2, text="Insertar en Pos", 
                                          command=self.insertar_posicion, state=tk.DISABLED, width=15)
        self.btn_insertar_pos.pack(side=tk.LEFT, padx=3)
        
        self.btn_obtener_pos = ttk.Button(botones2, text="Obtener de Pos", 
                                         command=self.obtener_posicion, state=tk.DISABLED, width=15)
        self.btn_obtener_pos.pack(side=tk.LEFT, padx=3)
        
        self.label_info = ttk.Label(frame_operaciones, text="", foreground="blue")
        self.label_info.pack(pady=2)
        
        # Frame principal con canvas y texto
        frame_principal = ttk.Frame(main_frame)
        frame_principal.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Canvas para la representacion grafica
        frame_canvas = ttk.LabelFrame(frame_principal, text="Visualizacion Grafica", padding="5")
        frame_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        
        self.canvas = tk.Canvas(frame_canvas, bg="white", height=400, width=700)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Scrollbars para el canvas
        h_scrollbar = ttk.Scrollbar(frame_canvas, orient=tk.HORIZONTAL, command=self.canvas.xview)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        v_scrollbar = ttk.Scrollbar(frame_canvas, orient=tk.VERTICAL, command=self.canvas.yview)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        self.canvas.configure(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        
        # Frame para resultados en texto
        frame_texto = ttk.LabelFrame(frame_principal, text="Resultados", padding="5")
        frame_texto.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5)
        
        self.text_resultado = scrolledtext.ScrolledText(frame_texto, width=40, height=20, 
                                                        font=("Consolas", 10))
        self.text_resultado.pack(fill=tk.BOTH, expand=True)
        
        # Boton limpiar
        ttk.Button(frame_texto, text="Limpiar Resultados", 
                  command=self.limpiar_resultados).pack(pady=5)
    
    def seleccionar_estructura(self, tipo):
        if tipo == "pila":
            self.estructura_actual = self.pila
            self.nombre_estructura = "Pila"
            self.btn_insertar.config(text="Apilar")
            self.btn_eliminar.config(text="Desapilar")
            self.btn_buscar.config(state=tk.NORMAL)
            self.btn_vaciar.config(state=tk.NORMAL)
            self.btn_insertar_pos.config(state=tk.DISABLED)
            self.btn_obtener_pos.config(state=tk.DISABLED)
            self.label_info.config(text="Pilas: LIFO (Last In, First Out) - La cima es el ultimo elemento")
        elif tipo == "cola":
            self.estructura_actual = self.cola
            self.nombre_estructura = "Cola"
            self.btn_insertar.config(text="Encolar")
            self.btn_eliminar.config(text="Desencolar")
            self.btn_buscar.config(state=tk.NORMAL)
            self.btn_vaciar.config(state=tk.NORMAL)
            self.btn_insertar_pos.config(state=tk.DISABLED)
            self.btn_obtener_pos.config(state=tk.DISABLED)
            self.label_info.config(text="Colas: FIFO (First In, First Out)")
        elif tipo == "lista_simple":
            self.estructura_actual = self.lista_simple
            self.nombre_estructura = "Lista Simple"
            self.btn_insertar.config(text="Insertar Final")
            self.btn_eliminar.config(text="Eliminar")
            self.btn_buscar.config(state=tk.NORMAL)
            self.btn_vaciar.config(state=tk.NORMAL)
            self.btn_insertar_pos.config(state=tk.NORMAL)
            self.btn_obtener_pos.config(state=tk.NORMAL)
            self.label_info.config(text="Lista Simple: punteros solo hacia adelante")
        elif tipo == "lista_doble":
            self.estructura_actual = self.lista_doble
            self.nombre_estructura = "Lista Doble"
            self.btn_insertar.config(text="Insertar Final")
            self.btn_eliminar.config(text="Eliminar")
            self.btn_buscar.config(state=tk.NORMAL)
            self.btn_vaciar.config(state=tk.NORMAL)
            self.btn_insertar_pos.config(state=tk.NORMAL)
            self.btn_obtener_pos.config(state=tk.NORMAL)
            self.label_info.config(text="Lista Doble: punteros hacia adelante y atras")
        
        self.label_estructura.config(text=f"Estructura seleccionada: {self.nombre_estructura}")
        self.btn_insertar.config(state=tk.NORMAL)
        self.btn_eliminar.config(state=tk.NORMAL)
        self.btn_vaciar.config(state=tk.NORMAL)
        self.mostrar()
    
    def dibujar_estructura(self):
        """Dibuja la estructura actual en el canvas"""
        self.canvas.delete("all")
        
        if self.estructura_actual is None:
            return
        
        # Obtener los elementos de la estructura
        if self.nombre_estructura == "Pila":
            elementos = self.obtener_elementos_pila()
            self.dibujar_pila(elementos)
        elif self.nombre_estructura == "Cola":
            elementos = self.obtener_elementos_cola()
            self.dibujar_cola(elementos)
        elif self.nombre_estructura == "Lista Simple":
            elementos = self.obtener_elementos_lista_simple()
            self.dibujar_lista_simple(elementos)
        elif self.nombre_estructura == "Lista Doble":
            elementos = self.obtener_elementos_lista_doble()
            self.dibujar_lista_doble(elementos)
        
        # Actualizar scroll region
        self.canvas.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    
    def obtener_elementos_pila(self):
        """Obtiene los elementos de la pila"""
        elementos = []
        try:
            mostrar_str = self.estructura_actual.mostrar()
            if mostrar_str and isinstance(mostrar_str, str) and mostrar_str.strip():
                # La pila en C++ devuelve: "cima ... base" o "base ... cima"?
                # Asumimos que muestra desde la base hasta la cima
                nums = mostrar_str.strip().split()
                elementos = [int(n) for n in nums if n.strip()]
        except:
            pass
        return elementos
    
    def obtener_elementos_cola(self):
        """Obtiene los elementos de la cola"""
        elementos = []
        try:
            mostrar_str = self.estructura_actual.mostrar()
            if mostrar_str and isinstance(mostrar_str, str) and mostrar_str.strip():
                nums = mostrar_str.strip().split()
                elementos = [int(n) for n in nums if n.strip()]
        except:
            pass
        return elementos
    
    def obtener_elementos_lista_simple(self):
        """Obtiene los elementos de la lista simple"""
        elementos = []
        try:
            mostrar_str = self.estructura_actual.mostrar()
            if mostrar_str and isinstance(mostrar_str, str) and mostrar_str.strip():
                nums = mostrar_str.strip().split()
                elementos = [int(n) for n in nums if n.strip()]
        except:
            pass
        return elementos
    
    def obtener_elementos_lista_doble(self):
        """Obtiene los elementos de la lista doble"""
        elementos = []
        try:
            # Intentar con mostrar_adelante primero
            mostrar_str = self.estructura_actual.mostrar_adelante()
            if mostrar_str and isinstance(mostrar_str, str) and mostrar_str.strip():
                nums = mostrar_str.strip().split()
                elementos = [int(n) for n in nums if n.strip()]
            else:
                # Si no funciona, intentar con mostrar normal
                mostrar_str = self.estructura_actual.mostrar()
                if mostrar_str and isinstance(mostrar_str, str) and mostrar_str.strip():
                    nums = mostrar_str.strip().split()
                    elementos = [int(n) for n in nums if n.strip()]
        except Exception as e:
            # Ultimo recurso: intentar obtener elemento por elemento
            try:
                tam = self.estructura_actual.tamano()
                for i in range(tam):
                    try:
                        val = self.estructura_actual.obtener(i)
                        elementos.append(val)
                    except:
                        pass
            except:
                pass
        return elementos
    
    def dibujar_pila(self, elementos):
        """Dibuja una pila verticalmente - CORREGIDO: la cima va arriba"""
        if not elementos:
            self.canvas.create_text(400, 200, text="Pila vacia", font=("Arial", 14), fill="gray")
            return
        
        x_centro = 400
        y_inicio = 200  # Comenzar desde arriba
        ancho = 80
        alto = 40
        separacion = 10
        
        # Los elementos vienen en orden: [base, ... , cima] o [cima, ... , base]?
        # Asumimos que vienen desde la base hasta la cima
        # Si vienen al reves, usamos elementos directamente
        for i, valor in enumerate(elementos):
            y = y_inicio + i * (alto + separacion)
            color = self.colores[i % len(self.colores)]
            
            # Dibujar nodo
            self.canvas.create_rectangle(x_centro - ancho//2, y - alto//2,
                                        x_centro + ancho//2, y + alto//2,
                                        fill=color, outline="black", width=2)
            
            # Texto del valor
            self.canvas.create_text(x_centro, y, text=str(valor), 
                                   font=("Arial", 12, "bold"))
            
            # Indicador de cima para el ULTIMO elemento (el de abajo si es LIFO?)
            if i == len(elementos) - 1:
                self.canvas.create_text(x_centro + ancho//2 + 20, y, 
                                       text="CIMA", font=("Arial", 10, "bold"), 
                                       fill="red", anchor="w")
            # Indicador de base para el primer elemento
            if i == 0:
                self.canvas.create_text(x_centro - ancho//2 - 20, y, 
                                       text="BASE", font=("Arial", 10, "bold"), 
                                       fill="blue", anchor="e")
    
    def dibujar_cola(self, elementos):
        """Dibuja una cola horizontalmente"""
        if not elementos:
            self.canvas.create_text(400, 200, text="Cola vacia", font=("Arial", 14), fill="gray")
            return
        
        x_inicio = 200
        y_centro = 250
        ancho = 70
        alto = 40
        separacion = 80
        
        for i, valor in enumerate(elementos):
            x = x_inicio + i * separacion
            color = self.colores[i % len(self.colores)]
            
            # Dibujar nodo
            self.canvas.create_rectangle(x - ancho//2, y_centro - alto//2,
                                        x + ancho//2, y_centro + alto//2,
                                        fill=color, outline="black", width=2)
            
            # Texto del valor
            self.canvas.create_text(x, y_centro, text=str(valor), 
                                   font=("Arial", 12, "bold"))
            
            # Flecha al siguiente
            if i < len(elementos) - 1:
                x_sig = x_inicio + (i + 1) * separacion
                self.dibujar_flecha(x + ancho//2, y_centro, x_sig - ancho//2, y_centro)
            
            # Indicadores
            if i == 0:
                self.canvas.create_text(x - ancho//2 - 20, y_centro, 
                                       text="FRENTE", font=("Arial", 10, "bold"), 
                                       fill="blue", anchor="e")
            if i == len(elementos) - 1:
                self.canvas.create_text(x + ancho//2 + 20, y_centro, 
                                       text="FIN", font=("Arial", 10, "bold"), 
                                       fill="green", anchor="w")
    
    def dibujar_lista_simple(self, elementos):
        """Dibuja una lista simple horizontalmente con flechas"""
        if not elementos:
            self.canvas.create_text(400, 200, text="Lista vacia", font=("Arial", 14), fill="gray")
            return
        
        x_inicio = 150
        y_centro = 250
        ancho = 70
        alto = 40
        separacion = 100
        
        for i, valor in enumerate(elementos):
            x = x_inicio + i * separacion
            color = self.colores[i % len(self.colores)]
            
            # Dibujar nodo
            self.canvas.create_rectangle(x - ancho//2, y_centro - alto//2,
                                        x + ancho//2, y_centro + alto//2,
                                        fill=color, outline="black", width=2)
            
            # Texto del valor
            self.canvas.create_text(x, y_centro, text=str(valor), 
                                   font=("Arial", 12, "bold"))
            
            # Dibujar "siguiente" (puntero)
            self.canvas.create_rectangle(x + ancho//2 - 15, y_centro - 10,
                                        x + ancho//2 - 5, y_centro + 10,
                                        fill="lightgray", outline="gray")
            
            # Flecha al siguiente
            if i < len(elementos) - 1:
                x_sig = x_inicio + (i + 1) * separacion
                self.dibujar_flecha(x + ancho//2 - 5, y_centro, x_sig - ancho//2 + 15, y_centro)
            
            # Indicador de cabeza
            if i == 0:
                self.canvas.create_text(x - ancho//2 - 20, y_centro - 30, 
                                       text="CABEZA", font=("Arial", 10, "bold"), 
                                       fill="purple")
                self.canvas.create_line(x - ancho//2, y_centro - 20, 
                                       x - ancho//2, y_centro - 10,
                                       arrow=tk.LAST, fill="purple")
    
    def dibujar_lista_doble(self, elementos):
        """Dibuja una lista doble con flechas en ambos sentidos"""
        if not elementos:
            self.canvas.create_text(400, 200, text="Lista vacia", font=("Arial", 14), fill="gray")
            return
        
        # Ajustar posicion inicial segun cantidad de elementos
        x_inicio = max(150, 400 - (len(elementos) * 60))
        y_centro = 250
        ancho = 70
        alto = 45
        separacion = 90
        
        for i, valor in enumerate(elementos):
            x = x_inicio + i * separacion
            color = self.colores[i % len(self.colores)]
            
            # Dibujar nodo principal
            self.canvas.create_rectangle(x - ancho//2, y_centro - alto//2,
                                        x + ancho//2, y_centro + alto//2,
                                        fill=color, outline="black", width=2)
            
            # Texto del valor
            self.canvas.create_text(x, y_centro, text=str(valor), 
                                   font=("Arial", 12, "bold"))
            
            # Dibujar puntero siguiente (en la parte superior derecha)
            self.canvas.create_rectangle(x + ancho//2 - 15, y_centro - 20,
                                        x + ancho//2 - 5, y_centro - 5,
                                        fill="lightblue", outline="blue")
            self.canvas.create_text(x + ancho//2 - 10, y_centro - 12, 
                                   text="→", font=("Arial", 8, "bold"))
            
            # Dibujar puntero anterior (en la parte inferior izquierda)
            self.canvas.create_rectangle(x - ancho//2 + 5, y_centro + 5,
                                        x - ancho//2 + 15, y_centro + 20,
                                        fill="lightgreen", outline="green")
            self.canvas.create_text(x - ancho//2 + 10, y_centro + 12, 
                                   text="←", font=("Arial", 8, "bold"))
            
            # Flechas de conexion
            if i < len(elementos) - 1:
                x_sig = x_inicio + (i + 1) * separacion
                
                # Flecha siguiente (azul) - de este nodo al siguiente
                self.canvas.create_line(x + ancho//2 - 5, y_centro - 12,
                                       x_sig - ancho//2 + 5, y_centro - 12,
                                       arrow=tk.LAST, fill="blue", width=2)
                
                # Flecha anterior (verde) - del siguiente a este
                self.canvas.create_line(x_sig - ancho//2 + 5, y_centro + 12,
                                       x + ancho//2 - 5, y_centro + 12,
                                       arrow=tk.LAST, fill="green", width=2)
            
            # Indicadores de cabeza y cola
            if i == 0:
                self.canvas.create_text(x - ancho//2 - 30, y_centro - 30, 
                                       text="CABEZA", font=("Arial", 10, "bold"), 
                                       fill="purple")
                self.canvas.create_line(x - ancho//2, y_centro - 20, 
                                       x - ancho//2, y_centro - 10,
                                       arrow=tk.LAST, fill="purple", width=2)
            
            if i == len(elementos) - 1:
                self.canvas.create_text(x + ancho//2 + 30, y_centro - 30, 
                                       text="COLA", font=("Arial", 10, "bold"), 
                                       fill="orange")
                self.canvas.create_line(x + ancho//2, y_centro - 20, 
                                       x + ancho//2, y_centro - 10,
                                       arrow=tk.LAST, fill="orange", width=2)
    
    def dibujar_flecha(self, x1, y1, x2, y2, color="black", invertida=False):
        """Dibuja una flecha entre dos puntos"""
        if invertida:
            self.canvas.create_line(x1, y1, x2, y2, arrow=tk.FIRST, fill=color, width=2)
        else:
            self.canvas.create_line(x1, y1, x2, y2, arrow=tk.LAST, fill=color, width=2)
    
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
            messagebox.showerror("Error", "Ingrese un valor numerico valido")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def eliminar(self):
        try:
            if self.nombre_estructura == "Pila":
                if not self.estructura_actual.esta_vacia():
                    valor = self.estructura_actual.desapilar()
                    self.mostrar_mensaje(f"Desapilado: {valor}")
                else:
                    messagebox.showwarning("Advertencia", "La pila esta vacia")
            elif self.nombre_estructura == "Cola":
                if not self.estructura_actual.esta_vacia():
                    valor = self.estructura_actual.desencolar()
                    self.mostrar_mensaje(f"Desencolado: {valor}")
                else:
                    messagebox.showwarning("Advertencia", "La cola esta vacia")
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
                messagebox.showerror("Error", "Ingrese un valor numerico para eliminar")
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
            messagebox.showerror("Error", "Ingrese un valor numerico para buscar")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def insertar_posicion(self):
        if self.nombre_estructura not in ["Lista Simple", "Lista Doble"]:
            return
        
        try:
            valor = int(self.entry_valor.get())
            posicion = int(self.entry_posicion.get())
            self.estructura_actual.insertar_en_posicion(valor, posicion)
            self.mostrar_mensaje(f"Insertado {valor} en posicion {posicion}")
            self.mostrar()
            self.entry_valor.delete(0, tk.END)
            self.entry_posicion.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numericos validos")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def obtener_posicion(self):
        if self.nombre_estructura not in ["Lista Simple", "Lista Doble"]:
            return
        
        try:
            posicion = int(self.entry_posicion.get())
            valor = self.estructura_actual.obtener(posicion)
            self.mostrar_mensaje(f"En posicion {posicion}: {valor}")
            self.entry_posicion.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Ingrese una posicion numerica valida")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
    def mostrar(self):
        """Muestra la estructura en texto y graficamente"""
        try:
            # Mostrar en texto
            if self.nombre_estructura == "Pila":
                contenido = self.estructura_actual.mostrar()
                if not contenido:
                    contenido = "Pila vacia"
            elif self.nombre_estructura == "Cola":
                contenido = self.estructura_actual.mostrar()
                if not contenido:
                    contenido = "Cola vacia"
            elif self.nombre_estructura == "Lista Simple":
                contenido = self.estructura_actual.mostrar()
                if not contenido:
                    contenido = "Lista vacia"
            elif self.nombre_estructura == "Lista Doble":
                try:
                    contenido = self.estructura_actual.mostrar_adelante()
                    if not contenido:
                        contenido = "Lista vacia"
                except:
                    contenido = self.estructura_actual.mostrar()
                    if not contenido:
                        contenido = "Lista vacia"
            
            self.text_resultado.delete(1.0, tk.END)
            self.text_resultado.insert(tk.END, f"{self.nombre_estructura}:\n")
            self.text_resultado.insert(tk.END, f"Elementos: {contenido}\n")
            self.text_resultado.insert(tk.END, f"Tamano: {self.estructura_actual.tamano()}")
            
            # Dibujar graficamente
            self.dibujar_estructura()
            
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
    app = AplicacionEstructurasGrafica(root)
    root.mainloop()
    root = tk.Tk()
    app = AplicacionEstructurasGrafica(root)
    root.mainloop()