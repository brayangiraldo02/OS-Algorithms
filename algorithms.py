from process import process

# Function for initializing objects based on the number of processes to be created
def initialize_processes(num_processes):
  processes = []
  for i in range(num_processes):
    name = "P" + str(i)
    burst_time = int(input("Enter Burst Time for Process " + name + ": "))
    arrival_time = int(input("Enter Arrival Time for Process " + name + ": "))
    priority = int(input("Enter Priority for Process " + name + ": "))
    processes.append(process(name, burst_time, arrival_time, priority))
    print("--------------------------------------------")
  return processes

# Function to print the details of the processes
def print_processes(processes):
  print("Processes:")
  for p in processes:
    print("Name: " + p.name + " | Burst Time: " + str(p.burst_time) + " | Arrival Time: " + str(p.arrival_time) + " | Priority: " + str(p.priority))

def main():
  num_processes = int(input("Enter the number of processes: "))
  print("--------------------------------------------")
  processes = initialize_processes(num_processes)
  print_processes(processes)

if __name__ == "__main__":
  main()