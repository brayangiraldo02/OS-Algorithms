import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec


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

        # Tabla de procesos
        table_ax = fig.add_subplot(gs[1])
        table_ax.axis('off')

        # Crear tabla de procesos
        table = table_ax.table(cellText=[[process.name, process.arrival_time, process.burst_time, process.priority,
                                          process.start_time, process.completion_time, process.waiting_time,
                                          process.system_time] for process in self.processes],
                               colLabels=['Nombre', 'T. llegada', 'T. ráfaga', 'Prioridad', 'T. inicio',
                                          'T. finalización', 'T. de espera', 'T. de sistema'],
                               loc='center')

        # Establecer tamaño de la fuente
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1, 1.5)

        # Tiempos de espera debajo de la tabla
        wait_times_ax = fig.add_subplot(gs[2])
        wait_times_ax.axis('off')
        wait_times_ax.text(0.5, 0.4, f"Tiempo de espera promedio: {self.avg_waiting_time:.2f}",
                           ha='center', va='center')
        wait_times_ax.text(0.5, 0.1, f"Tiempo de sistema promedio: {self.avg_system_time:.2f}",
                            ha='center', va='center')

        plt.show()

    def calc_stats(self):
        self.avg_system_time = sum([process.system_time for process in self.processes]) / len(self.initial_processes)
        self.avg_waiting_time = sum([process.waiting_time for process in self.processes]) / len(self.initial_processes)
