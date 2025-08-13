from algorithms.fcfs import fcfs_scheduling
from algorithms.sstf import sstf_scheduling
from algorithms.scan import scan_scheduling
from algorithms.look import look_scheduling
from visualization.visualize import visualize_gantt_chart, visualize_seek_sequence
from data import processes, requests, head_start, disk_size, direction
import matplotlib.pyplot as plt

# FCFS
scheduled_processes = fcfs_scheduling(processes)

# SSTF
seek_sequence_sstf, _ = sstf_scheduling(requests, head_start)

# SCAN
seek_sequence_scan, _ = scan_scheduling(requests, head_start, disk_size, direction)

# LOOK
seek_sequence_look, _ = look_scheduling(requests, head_start, direction)

# Visualize
fig, axs = plt.subplots(4, 1, figsize=(12, 16))

# Assign different colors for each algorithm
fcfs_color = "skyblue"
sstf_color = "orange"
scan_color = "green"
look_color = "blue"

# Visualize each algorithm
visualize_gantt_chart(scheduled_processes, axs[0], "FCFS Scheduling", fcfs_color)
visualize_seek_sequence(seek_sequence_sstf, "SSTF Scheduling", axs[1], sstf_color)
visualize_seek_sequence(seek_sequence_scan, "SCAN Scheduling", axs[2], scan_color)
visualize_seek_sequence(seek_sequence_look, "LOOK Scheduling", axs[3], look_color)

plt.tight_layout()
plt.show()
