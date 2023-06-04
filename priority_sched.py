# priority_sched.py
def priority_sched(processes, burst_time, priorities):
    n = len(processes)
    waiting_time = [0]*n
    turnaround_time = [0]*n

    proc_burst_priority = sorted(zip(processes, burst_time, priorities), key=lambda x: x[2])

    for i in range(1, n):
        waiting_time[i] = proc_burst_priority[i - 1][1] + waiting_time[i - 1]

    for i in range(n):
        turnaround_time[i] = proc_burst_priority[i][1] + waiting_time[i]

    avg_wait = sum(waiting_time) / n
    avg_turnaround = sum(turnaround_time) / n

    return avg_wait, avg_turnaround
