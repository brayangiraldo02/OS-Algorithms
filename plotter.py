import matplotlib.pyplot as plt


class Plotter:
    def __init__(self, processes):
        self.processes = processes

    def plot_gantt_chart(self):
        # Crear listas para almacenar las etiquetas y los tiempos de inicio/fin
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

        # Establecer límites del eje X
        ax.set_xlim(0, total_duration)

        # Mostrar el gráfico
        plt.show()