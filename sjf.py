class Sjf:
  def __init__(self, processes):
    self.processes = processes

  def run(self):
    next_start_time = 0
    pending_processes = self.processes.copy()
    completed_processes = []

    while pending_processes:
      eligible_processes = [p for p in pending_processes if p.arrival_time <= next_start_time]

      if eligible_processes:
        eligible_processes.sort(key=lambda x: x.burst_time)
        current_process = eligible_processes.pop(0)

        current_process.start_time = next_start_time
        current_process.completion_time = next_start_time

        for bt in range(current_process.burst_time):
          current_process.completion_time += 1
          print("Process " + current_process.name + " completed at: " + str(current_process.completion_time))

        current_process.waiting_time = current_process.start_time - current_process.arrival_time
        current_process.system_time = current_process.completion_time - current_process.arrival_time
        next_start_time = current_process.completion_time

        completed_processes.append(current_process)
        pending_processes.remove(current_process)
        print("--------------------------------------------")

      else:
        next_start_time += 1

    return completed_processes