# Process Scheduling Algorithms

## Introduction
This Python script implements three process scheduling algorithms: FCFS (First-Come, First-Served), SJF (Shortest Job First), and RR (Round Robin). It includes a class `Process` with attributes such as name, arrival time, burst time, start time, and end time. The script also utilizes the `collections.deque` for the Round Robin algorithm and `matplotlib.pyplot` for visualizing the Gantt chart.

## Classes and Functions
### Process Class
- `Process(name, arrival_time, burst_time)`: Initializes a process with the given attributes.

### Scheduling Functions
- `fcfs(processes)`: Implements the FCFS scheduling algorithm and returns the Gantt chart.
- `sjf(processes)`: Implements the SJF scheduling algorithm and returns the Gantt chart.
- `rr(processes, time_quantum)`: Implements the Round Robin scheduling algorithm with a specified time quantum and returns the Gantt chart.

### Gantt Chart Visualization
- `draw_gantt_chart(gantt_chart)`: Uses `matplotlib.pyplot` to draw and display the Gantt chart based on the provided Gantt chart data.

## Main Execution
- `main()`: Initializes a list of processes and calls `show_menu()` to allow the user to choose a scheduling algorithm.
- `show_menu(processes)`: Displays a menu for selecting a scheduling algorithm, takes user input, and calls the corresponding scheduling function.

## Sample Data
The script includes a sample list of processes (`processes`) with their names, arrival times, and burst times.

## Execution
The `main()` function is executed, initiating the program and prompting the user to choose a scheduling algorithm. The selected algorithm's Gantt chart is then displayed using the `draw_gantt_chart()` function.

