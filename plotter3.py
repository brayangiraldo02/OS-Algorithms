import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import tkinter as tk
from tkinter import ttk


class Plotter:
    def __init__(self, initial_processes, processes):
        self.initial_processes = initial_processes
        self.processes = processes

    def plot_gantt_chart(self):
        # Crear listas para almacenar las etiquetas y los tiempos de inicio/fin
        self.calc_stats()
        labels = [process.name for process in self.processes]
        start_times = [process.start_time for process in self.processes]
        completion_times = [process.completion_time for process in self.processes]

        # Calcular la duración total del gráfico de Gantt
        total_duration = max(completion_times) + 2

        # Crear un gráfico de Gantt y una tabla utilizando GridSpec
        fig = plt.figure(figsize=(10, 6))
        gs = GridSpec(3, 1, height_ratios=[1, 1, 0.2], hspace=0.3)

        # Gráfico de Gantt
        ax = fig.add_subplot(gs[0])

        # Colores
        colors = plt.cm.Paired(range(len(self.processes)))

        # Dibujar barras horizontales para cada proceso
        for i, label in enumerate(labels):
            ax.barh(label, completion_times[i] - start_times[i], left=start_times[i], color=colors[i])

        # Establecer etiquetas y título
        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Procesos')
        ax.set_title('Gráfico de Gantt')

        # Establecer límites del eje X
        ax.set_xlim(0, total_duration)

        # Mostrar cuadrícula en el gráfico de Gantt
        ax.grid(True, linestyle='--', alpha=0.7)

        # Dividir la figura y crear otra figura para la tabla
        fig2, table_ax = plt.subplots(figsize=(10, 3))
        table_ax.axis('off')

        # Crear tabla de procesos
        table = table_ax.table(cellText=[[process.name, process.arrival_time, process.burst_time, process.priority,
                                          process.start_time, process.completion_time, process.waiting_time,
                                          process.system_time] for process in self.processes],
                               colLabels=['Nombre', 'T. llegada', 'T. ráfaga', 'Prioridad', 'T. inicio',
                                          'T. finalización', 'T. de espera', 'T. de sistema'],
                               loc='center')

        # Establecer tamaño de la fuente
        table.auto_set_font_size(True)
        # table.set_fontsize(10)
        table.auto_set_column_width(col=list(range(len(self.processes) + 1)))

        table.scale(1, 1.5)

        # Ajustar el tamaño de la figura para incluir la tabla completa
        fig.tight_layout()

        # Obtener la máxima posición en Y del gráfico de Gantt
        max_y_position = ax.get_ylim()[1]

        # Calcular las posiciones en Y para los textos debajo de la tabla
        wait_times_y1 = max_y_position + 0.05
        wait_times_y2 = wait_times_y1 + 0.4

        # Tiempos de espera debajo de la tabla
        wait_times_ax = fig.add_subplot(gs[2])
        wait_times_ax.axis('off')
        wait_times_ax.annotate(f"Tiempo de espera promedio: {self.avg_waiting_time:.2f}",
                              xy=(0.5, wait_times_y1), xycoords='axes fraction',
                              ha='center', va='center')
        wait_times_ax.annotate(f"Tiempo de sistema promedio: {self.avg_system_time:.2f}",
                              xy=(0.5, wait_times_y2), xycoords='axes fraction',
                              ha='center', va='center')

        plt.show()
        
    def plot_table(self):
         # Crear ventana principal
        root = tk.Tk()
        root.title('Tabla de Procesos')

        # Crear el Treeview
        tree = ttk.Treeview(root)
        tree["columns"] = ("Nombre", "T. llegada", "T. ráfaga", "Prioridad", "T. inicio",
                           "T. finalización", "T. de espera", "T. de sistema")

        # Configurar las columnas
        tree.column("#0", width=0, stretch=tk.NO)  # Columna oculta
        tree.column("Nombre", anchor=tk.W, width=100)
        tree.column("T. llegada", anchor=tk.CENTER, width=80)
        tree.column("T. ráfaga", anchor=tk.CENTER, width=80)
        tree.column("Prioridad", anchor=tk.CENTER, width=80)
        tree.column("T. inicio", anchor=tk.CENTER, width=80)
        tree.column("T. finalización", anchor=tk.CENTER, width=100)
        tree.column("T. de espera", anchor=tk.CENTER, width=100)
        tree.column("T. de sistema", anchor=tk.CENTER, width=100)

        # Configurar las cabeceras de las columnas
        tree.heading("#0", text="", anchor=tk.W)
        tree.heading("Nombre", text="Nombre", anchor=tk.W)
        tree.heading("T. llegada", text="T. llegada", anchor=tk.CENTER)
        tree.heading("T. ráfaga", text="T. ráfaga", anchor=tk.CENTER)
        tree.heading("Prioridad", text="Prioridad", anchor=tk.CENTER)
        tree.heading("T. inicio", text="T. inicio", anchor=tk.CENTER)
        tree.heading("T. finalización", text="T. finalización", anchor=tk.CENTER)
        tree.heading("T. de espera", text="T. de espera", anchor=tk.CENTER)
        tree.heading("T. de sistema", text="T. de sistema", anchor=tk.CENTER)

        # Insertar datos en la tabla
        for process in self.processes:
          tree.insert("", "end", values=(process.name, process.arrival_time, process.burst_time,
                                           process.priority, process.start_time, process.completion_time,
                                           process.waiting_time, process.system_time))
        

        # Agregar el Treeview a la ventana
        tree.pack(expand=True, fill=tk.BOTH)



        # Iniciar el bucle principal de la aplicación
        root.mainloop()

    def calc_stats(self):
        self.avg_system_time = sum([process.system_time for process in self.processes]) / len(self.initial_processes)
        self.avg_waiting_time = sum([process.waiting_time for process in self.processes]) / len(self.initial_processes)
