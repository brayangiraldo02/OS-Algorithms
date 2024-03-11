import matplotlib.animation as animation
import matplotlib.pyplot as plt

class Plotter:
    def __init__(self, processes):
        self.processes = processes
        self.finished_processes = []
        self.avg_waiting_time = 0
        self.avg_system_time = 0

    def plot_gantt_chart(self):
        # Crear un gráfico de Gantt inicial vacío
        fig, ax = plt.subplots()

        # Colores
        colors = plt.cm.Paired(range(len(self.processes)))

        # Establecer etiquetas y título
        ax.set_xlabel('Tiempo')
        ax.set_ylabel('Procesos')
        ax.set_title('Gráfico de Gantt')

        # Mostrar promedio de tiempo de espera y tiempo de sistema en la parte inferior del gráfico
        fig.text(0.5, 0, f"Tiempo de espera promedio: {self.avg_waiting_time:.2f}", ha='center', va='center', fontsize=8)
        fig.text(0.5, -0.05, f"Tiempo de sistema promedio: {self.avg_system_time:.2f}", ha='center', va='center', fontsize=8)

        # Crear la función de actualización para la animación
        def update(frame):
            # Borra el gráfico anterior
            ax.cla()

            # Dibujar barras horizontales para los procesos en ejecución
            self.draw_running_processes(ax, frame, colors)

            # Dibujar barras horizontales para los procesos terminados
            self.draw_finished_processes(ax, colors)

            # Establecer etiquetas y título
            ax.set_xlabel('Tiempo')
            ax.set_ylabel('Procesos')
            ax.set_title('Gráfico de Gantt')

            # Establecer límites del eje X
            ax.set_xlim(0, frame + 2)

            # Mostrar promedio de tiempo de espera y tiempo de sistema en la parte inferior del gráfico
            fig.text(0.5, 0, f"Tiempo de espera promedio: {self.avg_waiting_time:.2f}", ha='center', va='center', fontsize=8)
            fig.text(0.5, -0.05, f"Tiempo de sistema promedio: {self.avg_system_time:.2f}", ha='center', va='center', fontsize=8)

        # Crear la animación
        ani = animation.FuncAnimation(fig, update, frames=self.get_animation_frames(), repeat=False)

        # Mostrar el gráfico
        plt.show()

    def draw_running_processes(self, ax, frame, colors):
        # Dibujar barras horizontales para los procesos en ejecución
        for process in self.processes:
            if process.start_time <= frame < process.completion_time:
                ax.barh(process.name, frame - process.start_time, left=process.start_time, color=colors[self.processes.index(process)])

    def draw_finished_processes(self, ax, colors):
        # Dibujar barras horizontales para los procesos terminados
        for process in self.finished_processes:
            ax.barh(process.name, process.completion_time - process.start_time, left=process.start_time, color=colors[self.processes.index(process)])

    def get_animation_frames(self):
        # Obtener la lista de frames para la animación
        all_frames = []
        for process in self.processes:
            all_frames.extend(range(process.start_time, process.completion_time + 1))
        return all_frames

    def calc_stats(self):
        self.avg_system_time = sum([process.system_time for process in self.processes])/len(self.processes)
        self.avg_waiting_time = sum([process.waiting_time for process in self.processes])/len(self.processes)

