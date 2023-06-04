# round_robin.py
def round_robin(processes, burst_time, quantum):
    n = len(processes)
    waiting_time = [0]*n
    remaining_time = burst_time.copy()
    t = 0  # El tiempo actual

    # Mientras hay procesos por terminar
    while True:
        done = True

        for i in range(len(processes)):
            if remaining_time[i] > 0:
                done = False  # Existen procesos pendientes

                if remaining_time[i] > quantum:
                    # Incrementa el tiempo total en quantum
                    t += quantum
                    # Decrementa el burst time en quantum
                    remaining_time[i] -= quantum
                else:
                    # Para los procesos restantes menos que quantum
                    t += remaining_time[i]
                    waiting_time[i] = t - burst_time[i]
                    # El burst time es cero ahora
                    remaining_time[i] = 0

        # Si todos los procesos están completos
        if done:
            break

    total_wt = sum(waiting_time)
    total_tat = sum([wt + bt for wt, bt in zip(waiting_time, burst_time)])

    avg_wait = total_wt / n
    avg_turnaround = total_tat / n

    return avg_wait, avg_turnaround
