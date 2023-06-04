# fcfs.py
def fcfs(processes, burst_time):
    n = len(processes)
    waiting_time = [0]*n
    turnaround_time = [0]*n
    waiting_time[0] = 0

    for i in range(1, n):
        waiting_time[i] = burst_time[i - 1] + waiting_time[i - 1]

    for i in range(n):
        turnaround_time[i] = burst_time[i] + waiting_time[i]
    
    avg_wait = sum(waiting_time) / n
    avg_turnaround = sum(turnaround_time) / n

    return avg_wait, avg_turnaround
