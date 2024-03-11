class Fifo:
  def __init__(self, processes):
    self.processes = processes

  def run(self):
    next_start_time = 0

    for p in self.processes:
      if p.arrival_time > next_start_time:
        next_start_time = p.arrival_time
        p.start_time = next_start_time
      else:
        p.start_time = next_start_time
      p.completion_time = next_start_time
      print("--------------------------------------------")
      print("Process " + p.name + " start at: " + str(p.start_time))
      print("Process " + p.name + " completed at: " + str(p.completion_time))

      # for bt in range(p.burst_time):
      #   p.completion_time += 1
      #   print("Process " + p.name + " completed at: " + str(p.completion_time))
      p.completion_time += p.burst_time

      p.waiting_time = p.start_time - p.arrival_time
      p.system_time = p.completion_time - p.arrival_time
      next_start_time = p.completion_time

    return self.processes
