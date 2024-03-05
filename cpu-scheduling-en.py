from collections import deque
import matplotlib.pyplot as plt

class Process:
    def __init__(self, name, arrival_time, burst_time):
        self.name = name
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.start_time = None
        self.end_time = None

def fcfs(processes):
    current_time = 0
    gantt_chart = []

    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time

        process.start_time = current_time
        process.end_time = current_time + process.burst_time
        current_time = process.end_time

        gantt_chart.append((process.name, process.start_time, process.end_time))

    return gantt_chart

def sjf(processes):
    processes.sort(key=lambda x: x.burst_time)  # Sort processes by burst time
    current_time = 0
    gantt_chart = []

    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time

        process.start_time = current_time
        process.end_time = current_time + process.burst_time
        current_time = process.end_time

        gantt_chart.append((process.name, process.start_time, process.end_time))

    return gantt_chart

def rr(processes, time_quantum):
    ready_queue = deque(processes)
    current_time = 0
    gantt_chart = []

    while ready_queue:
        process = ready_queue.popleft()

        if current_time < process.arrival_time:
            current_time = process.arrival_time

        process.start_time = current_time

        if process.burst_time <= time_quantum:
            process.end_time = current_time + process.burst_time
            current_time = process.end_time
            gantt_chart.append((process.name, process.start_time, process.end_time))
        else:
            process.burst_time -= time_quantum
            current_time += time_quantum
            ready_queue.append(process)
            gantt_chart.append((process.name, process.start_time, current_time))

    return gantt_chart

def draw_gantt_chart(gantt_chart):
    fig, ax = plt.subplots()

    # Set y-axis range
    ax.set_ylim(0, 1)

    # Set x-axis range
    total_time = gantt_chart[-1][2]
    ax.set_xlim(0, total_time)

    # Hide y-axis ticks
    ax.yaxis.set_visible(False)

    # Define color variable
    colors = ['#FF6F61', '#FFD166', '#06D6A0', '#118AB2', '#073B4C']  # Add more colors if needed

    # Draw Gantt chart bars
    for i, task in enumerate(gantt_chart):
        start_time = task[1]
        end_time = task[2]
        duration = end_time - start_time

        ax.broken_barh([(start_time, duration)], (0.2, 0.6), facecolors=colors[i % len(colors)])

        # Label task name above the Gantt chart bar
        ax.text(start_time + duration / 2, 0.5, task[0], ha='center', va='center')

    # Show Gantt chart
    plt.show()

def main():
    processes = [
        Process("P1", 0, 5),
        Process("P2", 1, 3),
        Process("P3", 2, 8),
        Process("P4", 3, 6),
        Process("P5", 4, 4)
    ]

    show_menu(processes)

def show_menu(processes):
    print("Please choose a scheduling algorithm:")
    print("1. FCFS (First-Come, First-Served)")
    print("2. SJF (Shortest Job First)")
    print("3. RR (Round Robin)")
    print("0. Exit the program")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        gantt_chart = fcfs(processes)
        draw_gantt_chart(gantt_chart)
    elif choice == 2:
        gantt_chart = sjf(processes)
        draw_gantt_chart(gantt_chart)
    elif choice == 3:
        time_quantum = int(input("Enter the time quantum size: "))
        gantt_chart = rr(processes, time_quantum)
        draw_gantt_chart(gantt_chart)
    elif choice == 0:
        return
    else:
        print("Invalid choice")

# Execute the main program
main()
