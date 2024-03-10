import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
from process import Process

class Plotter:
    def __init__(self, processes):
        self.processes = processes
        self.fig, self.ax = plt.subplots()

    def plot_gantt_chart(self):
        colors = plt.cm.Paired(range(len(self.processes)))

        for i, process in enumerate(self.processes):
            start_time = process.start_time
            end_time = process.completion_time

            self.ax.barh(process.name, end_time - start_time, left=start_time, color=colors[i], label=process.name)

        self.ax.set_xlabel('Tiempo')
        self.ax.set_ylabel('Procesos')
        self.ax.set_title('Diagrama de Gantt')

        # Ajusta el formato del eje x para mostrar el tiempo
        self.ax.xaxis_date()
        self.ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))

        plt.legend()
        plt.show()

# Ejemplo de uso:
if __name__ == "__main__":
    from datetime import timedelta

    # Supongamos que tienes una lista de procesos
    processes = [
        Process(name="P1", burst_time=5, arrival_time=0, priority=2),
        Process(name="P2", burst_time=3, arrival_time=2, priority=1),
        Process(name="P3", burst_time=4, arrival_time=4, priority=3),
    ]

    # Simula la asignación de tiempos de inicio y finalización a los procesos
    for i, process in enumerate(processes):
        process.start_time = datetime.now() + timedelta(seconds=i * 2)
        process.completion_time = process.start_time + timedelta(seconds=process.burst_time)

    # Crea y muestra el diagrama de Gantt
    gantt_chart = GanttChart(processes)
    gantt_chart.plot_gantt_chart()
