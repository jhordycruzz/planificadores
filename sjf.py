# sjf.py
def sjf(processes, burst_time):
    n = len(processes)
    waiting_time = [0]*n
    turnaround_time = [0]*n
    completed = [False]*n
    total_burst = sum(burst_time)

    current_time = 0
    while current_time < total_burst:
        min_burst = float('inf')
        for i in range(n):
            if not completed[i] and burst_time[i] < min_burst:
                current_process = i
                min_burst = burst_time[i]
        waiting_time[current_process] = current_time
        current_time += burst_time[current_process]
        turnaround_time[current_process] = waiting_time[current_process] + burst_time[current_process]
        completed[current_process] = True

    avg_wait = sum(waiting_time) / n
    avg_turnaround = sum(turnaround_time) / n

    return avg_wait, avg_turnaround
