from process import Process

class Round_robin:
  def __init__(self, processes, quantum):
    self.processes = processes
    self.quantum = quantum
    self.completed_processes = []  

  def run(self):
    next_start_time = 0

    while self.processes:
      current_process = self.processes.pop(0)

      burst_time = current_process.burst_time
      if current_process.arrival_time > next_start_time:
        next_start_time = current_process.arrival_time
        current_process.start_time = next_start_time
      else:
        current_process.start_time = next_start_time
      current_process.completion_time = next_start_time

      arrival_time = current_process.arrival_time
      if current_process.burst_time >= self.quantum:
        current_process.completion_time += self.quantum
        current_process.burst_time -= self.quantum
        next_start_time += self.quantum
        current_process.arrival_time = next_start_time
        self.processes.append(current_process)
        save_process = current_process
      else:
        current_process.completion_time += current_process.burst_time
        next_start_time += current_process.burst_time

      if burst_time != 0:
        name = current_process.name
        waiting_time = current_process.start_time - arrival_time
        system_time = current_process.completion_time - arrival_time
        priority = 0

        new_process = Process(name, burst_time, arrival_time, priority)
        new_process.start_time = current_process.start_time
        new_process.completion_time = current_process.completion_time
        new_process.waiting_time = waiting_time
        new_process.system_time = system_time

        print("--------------------------------------------")
        print("Process " + new_process.name + " start at: " + str(new_process.start_time))
        print("Process " + new_process.name + " completed at: " + str(new_process.completion_time))

        self.completed_processes.append(new_process)

        prev_process = save_process

        if self.processes[0].arrival_time > next_start_time:
          if prev_process.arrival_time <= next_start_time and prev_process.burst_time > 0:
            self.processes.insert(0, prev_process)
            self.processes.pop()

    return self.completed_processes