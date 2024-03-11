import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, processes):
        self.processes = processes
        

    def plot_gantt_chart(self):
        # Crear listas para almacenar las etiquetas y los tiempos de inicio/fin
        self.calc_stats()
        labels = [process.name for process in self.processes]
        start_times = [process.start_time for process in self.processes]
        completion_times = [process.completion_time for process in self.processes]

        # Calcular la duración total del gráfico de Gantt
        total_duration = max(completion_times) + 2

        # Crear un gráfico de Gantt
        fig, ax = plt.subplots()

        # Colores
        colors = plt.cm.Paired(range(len(self.processes)))

        # Dibujar barras horizontales para cada proceso
        for i, label in enumerate(labels):
            ax.barh(label, completion_times[i] - start_times[i], left=start_times[i], color=colors[i])

        # Establecer etiquetas y título
        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Procesos')
        ax.set_title('Gráfico de Gantt')
        
				# # Mostrar promedio de tiempo de espera y tiempo de sistema en la parte inferior del gráfico
        ax.text(total_duration / 2, 0.1, f"Tiempo de espera promedio: {self.avg_waiting_time:.2f}", ha='center', va='center')
        ax.text(total_duration / 2, 0.2, f"Tiempo de sistema promedio: {self.avg_system_time:.2f}", ha='center', va='center')

        # Establecer límites del eje X
        ax.set_xlim(0, total_duration)
        
        plt.show()

    def calc_stats(self):
        self.avg_system_time = sum([process.system_time for process in self.processes])/len(self.processes)
        self.avg_waiting_time = sum([process.waiting_time for process in self.processes])/len(self.processes)


