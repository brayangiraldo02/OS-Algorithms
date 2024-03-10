import tkinter as tk
from tkinter import ttk
from process import Process
from fifo import Fifo
from sjf import Sjf
from plotter import Plotter


class Controller:
  def __init__(self):
    self.selected_algorithm = None
    self.processes = []
    self.processes_quantity = 0
    self.get_algorithm()

  def get_processes(self):
    pass

  def set_processes(self):
    pass

  def get_algorithm(self):
    root = tk.Tk()
    root.title("Seleccionar Algoritmo")
    root.geometry("300x200")

    label = ttk.Label(root, text="Selecciona un algoritmo:")
    label.pack(pady=10)

    algorithms = ["FIFO", "SJF", "PRIORIDAD"]
    
    for algorithm in algorithms:
      button = ttk.Button(root, text=algorithm, 
                          command=lambda a=algorithm: self.select_algorithm(a,root),
                          style='Blue.TButton')
      button.pack(pady=5)
    
    # disabled_button = ttk.Button(root, text="Round Robbin", state="disabled")
    # disabled_button.pack(pady=5)
    style = ttk.Style()
    style.configure('Blue.TButton', foreground='white', background='blue')

    root.mainloop()

  def select_algorithm(self, algorithm,root):
      self.selected_algorithm = algorithm
      root.destroy()
      self.get_processes_quantity()

  def get_processes_quantity(self):
    root = tk.Tk()
    root.title("Cantidad de Procesos")
    root.geometry("300x200")

    label = ttk.Label(root, text="Ingresa la cantidad de procesos:")
    label.pack(pady=10)

    entry = ttk.Entry(root)
    entry.pack(pady=5)

    button = ttk.Button(root, text="Aceptar", 
                        command=lambda: self.set_processes_quantity(entry.get(), root),
                        style='Blue.TButton')
    button.pack(pady=5)

    style = ttk.Style()
    style.configure('Blue.TButton', foreground='white', background='blue')

    root.mainloop()

  def set_processes_quantity(self, quantity, root):
    self.processes_quantity = int(quantity)
    root.destroy()
    self.get_processes(self.processes_quantity)

  def get_processes(self, quantity):
    for process in range(quantity):
      self.get_individual_process(process)
  

  def get_individual_process(self, process_number):
    root = tk.Tk()
    root.title(f"Proceso {process_number}")
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
    if self.selected_algorithm == "FIFO":
      fifo = Fifo(self.processes)
      self.solution = fifo.run()
    elif self.selected_algorithm == "SJF":
      sjf = Sjf(self.processes)
      self.solution = sjf.run()
    for p in self.solution:
      print(p.__dict__)

    self.plot_solution()
    
  def plot_solution(self):
    plotter = Plotter(self.solution)
    plotter.plot_gantt_chart()
    
      
    
controller = Controller()
print(controller.selected_algorithm)