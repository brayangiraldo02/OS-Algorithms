import tkinter as tk
from tkinter import ttk
from process import Process
from fifo import Fifo
from sjf import Sjf
from round_robin import Round_robin
from priority import Priority
from plotter4 import Plotter
from PIL import Image, ImageTk


class Controller:
  def __init__(self):
    self.selected_algorithm = None
    self.processes = []
    self.initial_processes = []
    self.processes_quantity = 0
    self.get_algorithm()

  def get_processes(self):
    pass

  def set_processes(self):
    pass

  def get_algorithm(self):
    root = tk.Tk()
    root.title("Seleccionar Algoritmo")
    # Eliminar bordes y decoración estándar
    # root.overrideredirect(True)

    # Obtener dimensiones de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcular coordenadas para centrar la ventana
    x_coordinate = (screen_width - 300) // 2
    y_coordinate = (screen_height - 200) // 2

    root.geometry(f"300x330+{x_coordinate}+{y_coordinate}")
   
     # Cargar la imagen desde el archivo ./assets/cpu.png
    image_path = "./assets/cpu.png"
    img = Image.open(image_path)
    img = img.resize((100, 100))  
    img = ImageTk.PhotoImage(img)

    # Crear un label para mostrar la imagen
    image_label = ttk.Label(root, image=img)
    image_label.image = img  # Guardar una referencia para evitar que la imagen sea eliminada por el recolector de basura
    image_label.pack(pady=5)
    
    label = ttk.Label(root, text="Selecciona un algoritmo:")
    label.pack(pady=10)

    algorithms = ["FIFO", "SJF", "PRIORIDAD", "ROUND ROBIN"]
    
    for algorithm in algorithms:
      button = ttk.Button(root, text=algorithm, 
                          command=lambda a=algorithm: self.select_algorithm(a,root),
                          style='Custom.TButton')
      button.pack(pady=5)
    
    style = ttk.Style()
    # Estilo del botón con bordes redondeados
    style.configure('Custom.TButton', 
                    foreground='#4CAF50', 
                    background='#4CAF50', 
                    padding=(5, 5), 
                    borderwidth=2, 
                    relief=tk.RAISED, 
                    borderradius=5)

    root.mainloop()

  def select_algorithm(self, algorithm,root):
      self.selected_algorithm = algorithm
      root.destroy()
      self.get_processes_quantity()

  def get_processes_quantity(self):
    root = tk.Tk()
    root.title("Cantidad de Procesos")
    # Obtener dimensiones de la pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcular coordenadas para centrar la ventana
    x_coordinate = (screen_width - 300) // 2
    y_coordinate = (screen_height - 200) // 2

    root.geometry(f"300x200+{x_coordinate}+{y_coordinate}")
   

    label = ttk.Label(root, text="Ingresa la cantidad de procesos:")
    label.pack(pady=10)

    entries=[]

    entry = ttk.Entry(root)
    entry.pack(pady=5)
    entries.append(entry)

    if self.selected_algorithm == "ROUND ROBIN":
      label = ttk.Label(root, text="Ingrese el valor de Q:")
      label.pack(pady=10)
      entry = ttk.Entry(root)
      entry.pack(pady=5)
      entries.append(entry)

    button = ttk.Button(root, text="Aceptar", 
                        command=lambda: self.set_processes_quantity_and_Q(entries, root),
                        style='Custom.TButton')
    button.pack(pady=5)

    style = ttk.Style()
    # Estilo del botón con bordes redondeados
    style.configure('Custom.TButton', 
                    foreground='#4CAF50', 
                    background='#4CAF50', 
                    padding=(5, 5), 
                    borderwidth=2, 
                    relief=tk.RAISED, 
                    borderradius=5)
    root.mainloop()

#--------------------------------------------------------------------------------
  def set_processes_quantity_and_Q(self, entries, root):
    if self.selected_algorithm == "ROUND ROBIN":
      self.processes_quantity = int(entries[0].get())
      self.Q = int(entries[1].get())
    else:
      self.processes_quantity = int(entries[0].get())
    
    root.destroy()
    self.get_processes(self.processes_quantity)


  def get_processes(self, quantity):
    for process in range(quantity):
      self.get_individual_process(process)
  

  def get_individual_process(self, process_number):
    root = tk.Tk()
    root.title(f"Proceso {process_number+1}")
    root.geometry("400x300")

    if self.selected_algorithm == "PRIORIDAD":
      labels = ["Nombre del proceso","Tiempo de ráfaga", "Tiempo de llegada",  "Prioridad"]
    else:
      labels = ["Nombre del proceso", "Tiempo de ráfaga", "Tiempo de llegada"]

    entries = []

    for i in range(len(labels)):
      label = ttk.Label(root, text=labels[i])
      label.grid(row=i, column=0, padx=10, pady=10)
      entry = ttk.Entry(root)
      entry.grid(row=i, column=1, padx=10, pady=10)
      entries.append(entry)

    button = ttk.Button(root, text="Guardar",
                        command=lambda: self.set_individual_process(entries, root),
                        style='Blue.TButton')
    button.grid(row=len(labels), columnspan=2, padx=10, pady=10)

    style = ttk.Style()
    style.configure('Blue.TButton', foreground='white', background='blue')

    # Centrar los elementos en la ventana
    for i in range(len(labels) + 1):  # +1 para incluir la fila del botón
        root.grid_rowconfigure(i, weight=1)

    for i in range(2):  # Dos columnas
        root.grid_columnconfigure(i, weight=1)

    # Centrar la ventana
    # root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))


    root.mainloop()
    

  def set_individual_process(self, entries, root):
   
    if self.selected_algorithm == "PRIORIDAD":
       process = Process(entries[0].get(), int(entries[1].get()), int(entries[2].get()), int(entries[3].get()))
    else:
       process = Process(entries[0].get(), int(entries[1].get()), int(entries[2].get()), 0)
    self.processes.append(process)
    root.destroy()
    if len(self.processes) == self.processes_quantity:
      self.processes.sort(key=lambda x: x.arrival_time)
      self.eval_algorithm()
  
  def eval_algorithm(self):
    self.initial_processes = self.processes.copy()
    if self.selected_algorithm == "FIFO":
      fifo = Fifo(self.processes)
      self.solution = fifo.run()
    elif self.selected_algorithm == "SJF":
      sjf = Sjf(self.processes)
      self.solution = sjf.run()
    elif self.selected_algorithm == "PRIORIDAD":
      priority = Priority(self.processes)
      self.solution = priority.run()
    elif self.selected_algorithm == "ROUND ROBIN":
      round_robin = Round_robin(self.processes, self.Q)
      self.solution = round_robin.run()
    for p in self.solution:
      print(p.__dict__)

    self.plot_solution()
    
  def plot_solution(self):
    plotter = Plotter(self.initial_processes, self.solution)
    plotter.plot_gantt_chart()
    plotter.plot_table()
    
      
    
controller = Controller()
print(controller.selected_algorithm)