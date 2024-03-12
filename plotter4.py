import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import font

class Plotter:
    def __init__(self, initial_processes, processes):
        self.initial_processes = initial_processes
        self.processes = processes

    def plot_gantt_chart(self):
        # Calcular estadísticas
        self.calc_stats()
        # Crear ventana principal
        root = tk.Tk()
        root.title('Gráfico de Gantt y Tabla de Procesos')

        # Configurar función para manejar el cierre de la ventana
        root.protocol("WM_DELETE_WINDOW", lambda: self.on_closing(root))

        # Crear el frame principal
        main_frame = tk.Frame(root)
        main_frame.pack(expand=True, fill=tk.BOTH)

        # Gráfico de Gantt
        fig, ax = plt.subplots(figsize=(8, 4))
        colors = plt.cm.Paired(range(len(self.processes)))
        labels = [process.name for process in self.processes]
        start_times = [process.start_time for process in self.processes]
        completion_times = [process.completion_time for process in self.processes]

        for i, label in enumerate(labels):
            ax.barh(label, completion_times[i] - start_times[i], left=start_times[i], color=colors[i])

        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Procesos')
        ax.set_title('Gráfico de Gantt')
        ax.grid(True, linestyle='--', alpha=0.7)

        # Agregar el gráfico a la interfaz de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=main_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(expand=True, fill=tk.BOTH)

        # Treeview (Tabla de procesos)
        tree = ttk.Treeview(main_frame)
        tree["columns"] = ("Nombre", "T. llegada", "T. ráfaga", "Prioridad", "T. inicio",
                           "T. finalización", "T. de espera", "T. de sistema")

        # Configurar columnas y encabezados de la tabla
        tree.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        tree.heading("#0", text="", anchor=tk.W)
        tree.column("Nombre", anchor=tk.W, width=100)
        tree.heading("Nombre", text="Nombre", anchor=tk.W)
        tree.column("T. llegada", anchor=tk.CENTER, width=80)
        tree.heading("T. llegada", text="T. llegada", anchor=tk.CENTER)
        tree.column("T. ráfaga", anchor=tk.CENTER, width=80)
        tree.heading("T. ráfaga", text="T. ráfaga", anchor=tk.CENTER)
        tree.column("Prioridad", anchor=tk.CENTER, width=80)
        tree.heading("Prioridad", text="Prioridad", anchor=tk.CENTER)
        tree.column("T. inicio", anchor=tk.CENTER, width=80)
        tree.heading("T. inicio", text="T. inicio", anchor=tk.CENTER)
        tree.column("T. finalización", anchor=tk.CENTER, width=100)
        tree.heading("T. finalización", text="T. finalización", anchor=tk.CENTER)
        tree.column("T. de espera", anchor=tk.CENTER, width=100)
        tree.heading("T. de espera", text="T. de espera", anchor=tk.CENTER)
        tree.column("T. de sistema", anchor=tk.CENTER, width=100)
        tree.heading("T. de sistema", text="T. de sistema", anchor=tk.CENTER)

        # Insertar datos en la tabla
        for process in self.processes:
            tree.insert("", "end", values=(process.name, process.arrival_time, process.burst_time,
                                           process.priority, process.start_time, process.completion_time,
                                           process.waiting_time, process.system_time))


        # Agregar la tabla a la interfaz de Tkinter
        tree.pack(expand=True, fill=tk.BOTH)

        bold_font = font.Font(weight="bold")  # Crear una fuente en negrita
        # Labels para la información calculada
        avg_waiting_label = tk.Label(main_frame, text=f"Tiempo de espera promedio: {self.avg_waiting_time:.2f}", font=bold_font)
        avg_waiting_label.pack()

        avg_system_label = tk.Label(main_frame, text=f"Tiempo de sistema promedio: {self.avg_system_time:.2f}", font=bold_font)
        avg_system_label.pack()

        # Iniciar el bucle principal de la aplicación
        root.mainloop()
        
    
    def calc_stats(self):
        self.avg_system_time = sum([process.system_time for process in self.processes]) / len(self.initial_processes)
        self.avg_waiting_time = sum([process.waiting_time for process in self.processes]) / len(self.initial_processes)

    def on_closing(self, root):
        # Esta función se llama al cerrar la ventana
        root.destroy()
        root.quit()