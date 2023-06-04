# srtf.py
def srtf(processes, arrival_time, burst_time):
    n = len(processes)
    waiting_time = [0]*n
    turnaround_time = [0]*n
    remaining_time = burst_time.copy()

    current_time = 0
    while True:
        min_burst = float('inf')
        for i in range(n):
            if arrival_time[i] <= current_time and remaining_time[i] < min_burst and remaining_time[i] > 0:
                current_process = i
                min_burst = remaining_time[i]
        if min_burst == float('inf'):
            break
        remaining_time[current_process] -= 1
        current_time += 1
        if remaining_time[current_process] == 0:
            waiting_time[current_process] = current_time - arrival_time[current_process] - burst_time[current_process]
            turnaround_time[current_process] = current_time - arrival_time[current_process]

    avg_wait = sum(waiting_time) / n
    avg_turnaround = sum(turnaround_time) / n

    return avg_wait, avg_turnaround
