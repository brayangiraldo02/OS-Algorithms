class Process():
  def __init__(self, name, burst_time, arrival_time, priority):
    self.name = name
    self.burst_time = burst_time
    self.arrival_time = arrival_time
    self.priority = priority
    self.waiting_time = 0
    self.system_time = 0
    self.start_time = 0
    self.completion_time = 0

