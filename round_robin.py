class Round_robin:
  def __init__(self, processes, quantum):
    self.processes = processes
    self.quantum = quantum
    self.completed_processes = []  # Lista para almacenar los procesos terminados

  def run(self):
    next_start_time = 0

    while self.processes:
      current_process = self.processes.pop(0)

      if current_process.arrival_time > next_start_time:
        next_start_time = current_process.arrival_time
        current_process.start_time = next_start_time
      else:
        current_process.start_time = next_start_time
      current_process.completion_time = next_start_time

      if current_process.burst_time > self.quantum:
        current_process.completion_time += self.quantum
        current_process.burst_time -= self.quantum
        next_start_time += self.quantum
        current_process.arrival_time = next_start_time
        self.processes.append(current_process)
      else:
        current_process.completion_time += current_process.burst_time
        next_start_time += current_process.burst_time

      current_process.waiting_time = current_process.start_time - current_process.arrival_time
      current_process.system_time = current_process.completion_time - current_process.arrival_time

      print("--------------------------------------------")
      print("Process " + current_process.name + " start at: " + str(current_process.start_time))
      print("Process " + current_process.name + " completed at: " + str(current_process.completion_time))

      self.completed_processes.append(current_process)

    return self.completed_processes