from process import process
from fifo import fifo
from sjf import sjf

# Function for initializing objects based on the number of processes to be created
def initialize_processes(num_processes):
  processes = []
  for i in range(num_processes):
    name = "P" + str(i+1)
    burst_time = int(input("Enter Burst Time for Process " + name + ": "))
    arrival_time = int(input("Enter Arrival Time for Process " + name + ": "))
    priority = int(input("Enter Priority for Process " + name + ": "))
    processes.append(process(name, burst_time, arrival_time, priority))
    print("--------------------------------------------")

  processes.sort(key=lambda x: x.arrival_time)
  return processes

# Function to print the details of the processes
def print_processes(processes):
  print("Processes:")
  for p in processes:
    print("Name: " + p.name + " | Burst Time: " + str(p.burst_time) + " | Arrival Time: " + str(p.arrival_time) + " | Priority: " + str(p.priority))

def algorithms(algorithm, processes):
  waiting_time = 0
  system_time = 0
  next_start_time = 0

  if algorithm == "FIFO":
    print("Using First In, First Out Algorithm")

    f = fifo(processes)
    completed_processes = f.run()

    waiting_time = sum(p.waiting_time for p in completed_processes)
    system_time = sum(p.system_time for p in completed_processes)
    print("--------------------------------------------")
    print("Average Waiting Time: " + str(waiting_time / len(processes)))
    print("Average System Time: " + str(system_time / len(processes)))

  elif algorithm == "SJF":
    print("Using Shortest Job First Algorithm")
    print("--------------------------------------------")
    
    s = sjf(processes)
    completed_processes = s.run()

    # Calcular tiempos promedio al finalizar todos los procesos
    waiting_time_sum = sum(p.waiting_time for p in completed_processes)
    system_time_sum = sum(p.system_time for p in completed_processes)

    print("Average Waiting Time: " + str(waiting_time_sum / len(completed_processes)))
    print("Average System Time: " + str(system_time_sum / len(completed_processes)))

  elif algorithm == "Priority":
    print("Using Priority Algorithm")
    # Implement Priority algorithm here

  else:
    print("Invalid Algorithm")

  return processes

def main():
  num_processes = int(input("Enter the number of processes: "))
  print("--------------------------------------------")
  processes = initialize_processes(num_processes)
  print_processes(processes)
  print("--------------------------------------------")
  algorithm = input("Enter the algorithm to be used: ")
  processes = algorithms(algorithm, processes)

if __name__ == "__main__":
  main()