# main.py
import fcfs
import sjf
import srtf
import round_robin
import priority_sched

def main():
    print("Elija un algoritmo de programación de procesos:")
    print("1. FCFS")
    print("2. SJF")
    print("3. SRTF")
    print("4. Round Robin")
    print("5. Prioridad")
    choice = int(input("Ingrese su elección: "))

    n = int(input("Ingrese el número de procesos: "))
    processes = list(range(n))
    burst_time = [0]*n
    for i in range(n):
        burst_time[i] = int(input(f"Ingrese el tiempo de burst para el proceso {i}: "))
    if choice == 1:
        avg_wait, avg_turnaround = fcfs.fcfs(processes, burst_time)
    elif choice == 2:
        avg_wait, avg_turnaround = sjf.sjf(processes, burst_time)
    elif choice == 3:
        arrival_time = [0]*n
        for i in range(n):
            arrival_time[i] = int(input(f"Ingrese el tiempo de llegada para el proceso {i}: "))
        avg_wait, avg_turnaround = srtf.srtf(processes, arrival_time, burst_time)
    elif choice == 4:
        quantum = int(input("Ingrese el quantum: "))
        avg_wait, avg_turnaround = round_robin.round_robin(processes, burst_time, quantum)
    elif choice == 5:
        priorities = [0]*n
        for i in range(n):
            priorities[i] = int(input(f"Ingrese la prioridad para el proceso {i}: "))
        avg_wait, avg_turnaround = priority_sched.priority_sched(processes, burst_time, priorities)
    else:
        print("Elección inválida")
        return

    print(f"Tiempo medio de espera: {avg_wait}")
    print(f"Tiempo medio de retorno: {avg_turnaround}")

if __name__ == "__main__":
    main()